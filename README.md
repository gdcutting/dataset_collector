# Dataset Collector Application

> This application is in a pre-release phase. I'm working on a basic 1.0 version for release in a few weeks (~late November 2023).

This is a python application that collects datasets. In the current version it is very much Work In Progress [WIP]. This initial test version uses the Kaggle API to retrieve a short list of current 'hot' (high activity) datasets and download them locally.

There are so many datasets out there that I'm often not sure where to start when working on new projects. So I decided to make a program that automatically downloads candidate datasets of interest to narrow down what to work on. As with my media collection, I often download large amounts of media that I might not use immediately, but want to have readily available when the time comes. As a data scientist / ML engineer / data engineer (or something), I feel obligated to collect and curate my own large collection of data. This desire is, admittedly, at least in part a pathology - but it is also very useful for work purposes... 

My initial idea is to use this tool to curate a GitHub repository of datasets. Yes, I know there are already a lot of them out there, but I want my own. GitHub, for example has (I believe) a 1GB storage for free accounts. That's not much space when you start collecting datasets, but still permits a useful collection of relatively small datasets. With cloud storage, though, the sky is the limit (100GB on Google Drive is $2/month), so without spending much money you could put together a pretty good collection of datasets for data science and ML projects.

There is **A LOT** of data available these days, and the volume grows by the second, but it can easily get overwhelming. There are so many places to get data, but it's tedious to have to visit multiple different websites to look for datasets. It seems that it would be helpful to allow users to search across multiple data sources from one place, download datasets all through one interface, and centralize them locally or at a remote repository or cloud storage account.

It also seems useful to be able to automate the process of gathering data - for example, to be able to download a certain number of datasets per day from specified sources under search conditions, and have the downloading and uploading take place automatically without the user having to click through multiple web interfaces.

The eventual goal is to build the application out to incorporate a number of important python and other features:
- an API
- YAML configuration
- CLI interface with argument parameters
- more data sources
- web interface
- multiple upload targets (Google Drive, iCloud, etc.)

and more. I am starting small and building one step at a time. If I'm dreaming all the way, this could eventually be not just a dataset collector, but the beginning of a larger tool that lets the user easily perform common data science tasks (like data profiling and exploratory analysis, training common model types, etc., etc.). I might never get there, but a dataset collector seems like a great place to start, for my own practical purposes and also for a portfolio project that checks a lot of boxes all in one place. So let's see where where the road will lead, one step at a time.
