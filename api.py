def llama(param):
    print(param)
    import subprocess
    import os
    # Open a new process with the 'main.exe' command and the specified parameter
    command = ['main.exe', '--model', 'ggml-llama-7b-q4.bin', '-p', param]
    p = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    # Read the output from the process
    output = p.stdout.read().decode().strip()

    # Close the process
    p.stdin.close()
    p.wait()

    # Return the output as a string
    return output
