# logs2json script
import json
import os
import mimetypes
import sys
import time

main_json = {"meta": {"build_name": "boo", "timestamp": time.time()}, "files": []}
mimetypes.init()
args_number = len(sys.argv)
if args_number < 2:
    raise Exception("no build name")
elif args_number < 3:
    raise Exception("no files to parse")

main_json["meta"]["build_name"] = sys.argv[1]
for i in range(2, args_number):
    test_file_name = sys.argv[i]
    with open(sys.argv[i], 'r') as f:
        file_field = {"name": "unknown", "content_type": "text/plain", "data": None}
        test_contents = f.read()
        file_field["name"] = os.path.basename(test_file_name)
        file_field["content_type"] = mimetypes.guess_type(test_file_name)[0]
        file_field["data"] = test_contents
        main_json["files"].append(file_field)

print(json.dumps(main_json, ensure_ascii=True, indent=4))

