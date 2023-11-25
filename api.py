import subprocess
def run_code(code):
    print('Got code: ', code)
    p = subprocess.Popen(['python', '-c', code], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    return stdout.decode(), stderr.decode()
    

if __name__ == '__main__':
    out,err = (run_code('print("Hello World")'))
    print(out)
    print(err)