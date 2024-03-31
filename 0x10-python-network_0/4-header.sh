#!/bin/bash
# take in a URL, sends a GET request to it, and displays the body
curl -sH "X-School-User-Id: 98" "${1}"
