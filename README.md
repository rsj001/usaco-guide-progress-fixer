# USACO Guide Progress Fixer

## Background

A simple program restore your problem progress on usaco.guide from your activity.

Chinese users may encounter network errors when logging in to Firebase, resulting in some strange consequences, such as the 'local progress override' leading to the loss of the progress.

However, I found that the progress was missing, but the activity and timestamp were still retained. In the downloaded 'userdata', you can rewrite json file to restore the progress.

It is a single file written in Python, coding with no maintainability and extensibility, but it is convenient to use.

## Usage

1. Make sure you have Python 3.

2. Put `main.py` and downloaded `usacoguide-userdata.json` into the same folder, execute `main.py` then load `usacoguide-userdata-fixed.json` to USACO Guide.

## Results

Results are shown in picture below:

![2022-11-19](https://user-images.githubusercontent.com/46622836/202840882-e28b0880-4081-4776-ba6e-2aeb1c2a6c76.png)
