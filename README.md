Script that dumps the skills from ESI, and categorizies them into a static file, readable by Python.

Project includes
- Script for generating the file
- File (for people that just want to download)

ESI routes used:

GET /universe/categories/{category_id}/ # pass in the id 16

GET /universe/groups/{group_id}/ # using the results of the above, for each group, get the skills

GET /universe/types/{type_id}/ # for each skill get the real name

Libaries used
- EsiPy

For help, contact me on Discord: PrivateZ#3944