# Dataset Collector Application

This is a python application that collects datasets. In the current version it is very much Work In Progress [WIP]. This initial test version uses the Kaggle API to retrieve a short list of current 'hot' (high activity) datasets and download them locally.

There are so many datasets out there that I'm often not sure where to start when working on new projects. So I decided to make a program that automatically downloads candidate datasets of interest to narrow down what to work on. As with my media collection, I often download large amounts of media that I might not use immediately, but want to have readily available when the time comes. As a data scientist / ML engineer / data engineer, I feel obligated to collect and curate my own large collection of data. This desire is, admittedly, at least in part a pathology - but it is also very useful for work purposes...

There is **A LOT** of data available these days, and the volume grows by the second, but it can easily get overwhelming. There are so many places to get data, but it's tedious to have to visit multiple different websites to look for data. It seems that it would be helpful to allow users to search across multiple data sources from one place, download datasets all through one interface, and centralize them locally or at a remote repository.

The eventual goal is to build the application out to incorporate a number of important python features:
- an API
- YAML configuration
- CLI interface with argument parameters
- more data sources

and more. I am starting small and building one step at a time.
