#!/usr/bin/env python3
'''
Ionut Pirva  
September 2021
'''

import subprocess, sys, os, shutil, sysconfig
from pprint import pprint
from python.functions.variables import f_check_env_variables

def f_terraform_init() -> str:
    '''
        terraform init
        the function stores the stdout and std error and returns it
    '''

    terraformDir = f_check_env_variables(var = ["terraformDir"])["terraformDir"]

    if not os.path.exists(terraformDir):
        print(f"ERROR Dir {terraformDir} does not exist.")
        return None

    terraformINITFile = f"{terraformDir}/.init"
    # write 123 to init; 0 is OK RC
    with open(terraformINITFile, 'w') as initFile:
        initFile.write("123")

    cmdTerraformINIT = "terraform init -no-color -force-copy -get=true"
    command = f"echo chdir to {terraformDir} && cd {terraformDir} && echo Running the command: {cmdTerraformINIT} && {cmdTerraformINIT}"

    try:
        cmdRun = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    except Exception as e:
        print(f"ERROR {str(e)} while running {command}")
        return None
    while True:
        cmdStdOutErr = cmdRun.stdout.readline()
        if cmdRun.poll() is not None:
            break
        if cmdStdOutErr:
            print(cmdStdOutErr.strip().decode())
    
    output = cmdRun.poll()
    outputReturnCode = cmdRun.returncode
    if outputReturnCode != 0:
        print(f"ERROR while running init command: {command}")
    else:
        print(f"SUCCESS while running init command: {command}")
    
    # write the init command output 0 if it was successful and different otherwise
    with open(terraformINITFile, 'w') as initFile:
        initFile.write(str(outputReturnCode))
    
    return output

def f_python_init(nsxClusterIP: str = None, nsxClusterUser: str = None, nsxClusterPass: str = None) -> str:
    '''
        init the env used by and with python
        NSX-T: download NSX OpenAPI schema, generates Python bindings, installs needed Python modules to use the bindings
    '''

    pythonDir = f_check_env_variables(var = ["pythonDir"])["pythonDir"]
    nsxOpenAPIBindingDir = f_check_env_variables(var = ["nsxOpenAPIBindingDir"])["nsxOpenAPIBindingDir"]

    if not os.path.exists(pythonDir):
        print(f"ERROR Dir {pythonDir} does not exist.")
        return None

    pythonINITFile = f"{pythonDir}/.init"
    # write 123 to init; 0 is OK RC
    with open(pythonINITFile, 'w') as initFile:
        initFile.write("123")

    nsxOpenAPISchema = f"{pythonDir}/nsx_api.json"
    
    # pythonSitePackages = sysconfig.get_paths()["purelib"]
    # pythonSitePackagesSwaggerClient = f"{pythonSitePackages}/swagger_client-*/swagger_client"
    pythonSitePackagesSwaggerClient = f"{nsxOpenAPIBindingDir}/swagger_client"
    # delete nsxOpenAPIBinding if it exists
    if os.path.exists(nsxOpenAPIBindingDir):
        print(f"Delete dir: {nsxOpenAPIBindingDir}")
        shutil.rmtree(nsxOpenAPIBindingDir)
    cmdGetNSXOpenAPI = (
        f"curl -w '\n' -k -u \"{nsxClusterUser}:{nsxClusterPass}\" --connect-timeout 5 --retry 3 --retry-delay 1 -X GET "
        f"https://{nsxClusterIP}/api/v1/spec/openapi/nsx_api.json > {nsxOpenAPISchema}"
        )
    cmdGenerateBindings = f"java -jar /usr/bin/swagger-codegen-cli.jar generate -i {nsxOpenAPISchema} -l python -o {nsxOpenAPIBindingDir}"
    # disable IPinfo bindings, for some reason it cannot be loaded
    # IPinfo is not needed 
    cmdElse1 = f"sed -i 's/^[^#]* IPinfo$/# &/I' {pythonSitePackagesSwaggerClient}/models/__init__.py"
    cmdElse2 = f"sed -i 's/^[^#]* IPinfo$/# &/I' {pythonSitePackagesSwaggerClient}/__init__.py"
    
    command = (
        f"echo chdir to {pythonDir} && cd {pythonDir} && "
        f"echo GET NSX OpenAPI Schema from: \"{cmdGetNSXOpenAPI}\" && {cmdGetNSXOpenAPI} && "
        f"echo Save the NSX OpenAPI Schema to: {nsxOpenAPISchema} && "
        f"echo Create OpenAPI Python Binding dir: {nsxOpenAPIBindingDir} && mkdir -p {nsxOpenAPIBindingDir} && "
        f"echo Generate Python Binding: {cmdGenerateBindings} && {cmdGenerateBindings} && "
        f"echo Install required Python modules && pip3 install -r {nsxOpenAPIBindingDir}/requirements.txt && "
        # I do not run setup, I decided to add the swagger_client path to python module path
        # f"echo Install swagger_client python module && python3 {nsxOpenAPIBindingDir}/setup.py install --user && "
        f"{cmdElse1} && {cmdElse2}"
    )

    try:
        cmdRun = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    except Exception as e:
        print(f"ERROR {str(e)} while running {command}")
        return None
    while True:
        cmdStdOutErr = cmdRun.stdout.readline()
        if cmdRun.poll() is not None:
            break
        if cmdStdOutErr:
            print(cmdStdOutErr.strip().decode())
    
    output = cmdRun.poll()
    outputReturnCode = cmdRun.returncode
    if outputReturnCode != 0:
        print(f"ERROR while running init command: {command}")
    else:
        print(f"SUCCESS while running init command: {command}")
    
    # write the init command output 0 if it was successful and different otherwise
    with open(pythonINITFile, 'w') as initFile:
        initFile.write(str(outputReturnCode))

    return output
