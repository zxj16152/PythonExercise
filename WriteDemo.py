import os.path
def main():
    if os.path.isfile("Presidents.txt"):
        print("存在")
        return
    outfile=open("Presidents.txt","w")
    outfile.write("Bill Clinton\n")
    outfile.write("George bush\n")
    outfile.close()

main()