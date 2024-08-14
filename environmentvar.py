#!/usr/bin/env python3

import os

# This function of the os module gets an specified value of an environment variable
stage = os.getenv("STAGE", default="dev").upper()

print(stage)

output = f"We're running in {stage}"

if stage.startswith("PROD"):
    output = "Danger - " + output

print(output)
