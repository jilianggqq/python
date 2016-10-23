#!/usr/bin/env python
# -*- coding: utf-8 -*-

with open('abc.txt', 'r') as f:
    res = f.read()
res = res.replace('./abc', '/root/tools/home/CS385/abc')
res = res.replace('./tel/file1', '/root/tools/home/CS385/tel/file1')
res = res.replace('./sch/file2', '/root/tools/home/CS385/sch/file2')

print res