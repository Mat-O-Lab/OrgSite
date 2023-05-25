---
layout: post
title: CSVToCSVW Update
subtitle: Major Refactor in CSVToCSVW v1.1.9
categories: Tools
tags: [CSVtoCSVW, Tools]
---

## Major Refactor in CSVToCSVW v1.1.9 [^fn1]

The Mat-O-Lab team has pushed a significant update to their CSVToCSVW tool, version 1.1.9. This version includes a big refactor with a lot of changes and tweaks. One of the major updates includes a new segmentation feature, which segments the whole CSV and categorizes parts into meta (csv:notes) and data (csv:tables) categories. There is no need for choice of separators anymore. Moreover, the image size has been reduced by switching to slim python [^fn2]

The Mat-O-Lab/CSVToCSVW repository is a tool that generates JSON-LD for various types of CSVs. It adopts the Vocabulary provided by w3c at CSVW to describe structure and information within. The tool also uses QUDT units ontology to lookup and describe units.

[^fn2]: [releasenotes](https://github.com/Mat-O-Lab/CSVToCSVW/releases)
[^fn1]: [source](https://github.com/Mat-O-Lab/CSVToCSVW)
