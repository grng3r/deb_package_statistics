#!/usr/bin/python3
"""Displays 10 packages with the most file associated with them depending on architecture"""

import sys
import os
import gzip as gz
import requests as r


#url of mirror server
URL = "http://ftp.uk.debian.org/debian/dists/stable/main/"

#block with size a bit less than stack size to avoid memory clogging
BLOCK_SZ = 60000

def download_contents_file(arch):
    """download compressed file"""
    res = r.get(URL)
    #check if mirror available
    if res.status_code != 200:
        print("[ERR] Mirror server not available at the moment, displaying results from previous download.")
        return 1

    else:
        #download file
        print("[-] Downloading file...\n")
        file_download = r.get(URL + "Contents-"+ arch + ".gz", stream = True)
        #check if file available on server
        if file_download.status_code != 200:
            print("[ERR] Requested file not available at the moment, displaying results from previous download.")
            return 1

        else:
            #unzip file
            gz_file_path = "Contents-" + arch + ".gz"
            file_path = "Contents-" + arch
            with open(gz_file_path, 'wb') as f:
                f.write(file_download.raw.read())
            unzip_file = unzip(gz_file_path, file_path, BLOCK_SZ)

            if unzip_file != 0:
                print("[ERR] Unziping file")
                return 1

            else:
                #remove ziped file
                if os.path.exists(gz_file_path):
                    print("[-] Removing gzip file...\n")
                    os.remove(gz_file_path)
                    return 0

                else:
                    print("[-] No gzip file...\n")
                    return 0

def unzip(source, destination, block_size):
    """unzip file"""
    print("[-] Unziping file...\n")
    with gz.open(source, 'rb') as s_file:
        with open(destination, 'wb') as d_file:
            while True:
                block = s_file.read(block_size)
                if not block:
                    break
                else:
                    d_file.write(block)
    return 0


def parse_contents_file(file_path):
    """from file read line from end to / and if the next line is different than the
    previous line add to dictionary if not increase value under key"""
    packages = {}
    print("[-] Processing file...\n")

    with open(file_path) as f:
        for line in f:
            index = line.rfind("/")
            package = line[index+1:].strip()

            if package not in packages:
                packages[package] = 1

            else:
                packages[package] += 1

        return packages


def get_top_10(packages, arch):
    """get top 10"""
    print("Top 10 for " + arch + " architecture\n")
    packages = sorted(packages.items(), reverse = True, key = lambda x: x[1])

    top_10 = packages[:10]
    for i, package in enumerate(top_10):
        print(str(i+1) + ". " + package[0] + "\t\t" + str(package[1]))

def main():
    """main function"""
    if len(sys.argv) != 2:
        error_mssg = """[ERR] Usage: ./package_statistics.py <architecture>
        Architectures:
        \tarmel,
        \tarmhf,
        \tarm64,
        \ti386,
        \tamd64,
        \tmips,
        \tmipsel,
        \tmips64el,
        \tppc64el,
        \ts390x,
        \tsource
        """
        raise ValueError("{}".format(error_mssg))

    else:
        arch = sys.argv[1]
        file_path = "Contents-" + arch
        if arch == "armel":
            file = download_contents_file(arch)
            if file == 0:
                packages = parse_contents_file(file_path)
                get_top_10(packages, arch)

            else:
                packages = parse_contents_file(file_path)
                get_top_10(packages, arch)


        elif arch == "armhf":
            file = download_contents_file(arch)
            if file == 0:
                packages = parse_contents_file(file_path)
                get_top_10(packages, arch)

            else:
                packages = parse_contents_file(file_path)
                get_top_10(packages, arch)



        elif arch == "arm64":
            file = download_contents_file(arch)
            if file == 0:
                packages = parse_contents_file(file_path)
                get_top_10(packages, arch)

            else:
                packages = parse_contents_file(file_path)
                get_top_10(packages, arch)


        elif arch == "i386":
            file = download_contents_file(arch)
            if file == 0:
                packages = parse_contents_file(file_path)
                get_top_10(packages, arch)

            else:
                packages = parse_contents_file(file_path)
                get_top_10(packages, arch)


        elif arch == "amd64":
            file = download_contents_file(arch)
            if file == 0:
                packages = parse_contents_file(file_path)
                get_top_10(packages, arch)

            else:
                packages = parse_contents_file(file_path)
                get_top_10(packages, arch)


        elif arch == "mips":
            file = download_contents_file(arch)
            if file == 0:
                packages = parse_contents_file(file_path)
                get_top_10(packages, arch)

            else:
                packages = parse_contents_file(file_path)
                get_top_10(packages, arch)


        elif arch == "mipsel":
            file = download_contents_file(arch)
            if file == 0:
                packages = parse_contents_file(file_path)
                get_top_10(packages, arch)

            else:
                packages = parse_contents_file(file_path)
                get_top_10(packages, arch)



        elif arch == "mips64el":
            file = download_contents_file(arch)
            if file == 0:
                packages = parse_contents_file(file_path)
                get_top_10(packages, arch)

            else:
                packages = parse_contents_file(file_path)
                get_top_10(packages, arch)


        elif arch == "ppc64el":
            file = download_contents_file(arch)
            if file == 0:
                packages = parse_contents_file(file_path)
                get_top_10(packages, arch)

            else:
                packages = parse_contents_file(file_path)
                get_top_10(packages, arch)

        elif arch == "s390x":
            file = download_contents_file(arch)
            if file == 0:
                packages = parse_contents_file(file_path)
                get_top_10(packages, arch)

            else:
                packages = parse_contents_file(file_path)
                get_top_10(packages, arch)


        elif arch == "source":
            file = download_contents_file(arch)
            if file == 0:
                packages = parse_contents_file(file_path)
                get_top_10(packages, arch)

            else:
                packages = parse_contents_file(file_path)
                get_top_10(packages, arch)


        else:
            raise ValueError("[ERR] Architecture not supported")



if __name__ == "__main__":
    main()
