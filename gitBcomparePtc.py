import os
from subprocess import call

def main():
    # path to beyond compare executable
    bcompare_path = "C:/Program Files/Beyond Compare 4/BCompare.exe"
    # PLACE YOUR GIT REPO PATH
    git_path = "C:/Users/dakin/Desktop/Restaurant-Distributed-Application-Using-gRPC-Framework/"
    # PLACE YOUR PTC SANDBOX PATH
    ptc_path = "C:/Users/dakin/Desktop/RestaurantServerPTC/Restaurant-Distributed-Application-Using-gRPC-Framework/"
    # READ FILE WITH GIT MODIFIED FILES
    text_file = open("files.txt","r")
    dir_path = text_file.readline()
    while dir_path:
        # CONSTRUCT GIT ABSOLUTE PATH
        git_source_path = os.path.join(git_path,dir_path)
        git_source_path = git_source_path[0:len(git_source_path)-1]
        # CONTRUCT PTC ABSOLUTE PATH
        ptc_source_path = os.path.join(ptc_path,dir_path)
        ptc_source_path = ptc_source_path[0:len(ptc_source_path)-1]
        # BYOND COMPARE ARGUMENT
        args = bcompare_path+" "+git_source_path+" "+ptc_source_path
        # EXECUTE COMPARATION
        call(args)
        # NEXT PATH
        dir_path = text_file.readline()

if __name__ == '__main__':
    main()
