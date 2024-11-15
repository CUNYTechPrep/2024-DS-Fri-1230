---
title: Fall Friday Practice
emoji: 👁
colorFrom: red
colorTo: indigo
sdk: streamlit
sdk_version: 1.40.1
app_file: app.py
pinned: false
short_description: fall-friday-practice
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

# Web Apps in 5 mins

## Deploying on HuggingFace

0. Create an huggingface access token and copy it into a text file, it looks something like this `hf_AsfdeaxQeXasdfdafaxuNxtzjWpHnKnet`.
0. Create a new huggingface space. 
0. Copy that huggingface space repo link. It will look something like this. `https://huggingface.co/spaces/KingZack/live-in-class-tuesday` 
0. In that text document with your access token, copy the repo link, then edit the link and by putting your access token followed by an @ symbol after the `//` and before the `huggingface.co/....` 
   * It will look something like this 
   * `https://hf_AsfdeaxQeXasdfdafaxuNxtzjWpHnKnet@huggingface.co/spaces/KingZack/live-in-class-tuesday`
0. Open the terminal on your machine, and do `git clone [the link above with your access token]`
0. Make your edits and changes.  
0. Do the tride and trusted.
   * `git add *`
   * `git commit -m 'my message here'`
   * `git push`
0. It will then ask you for your password. and the password is your access token.  So just paste your access token as your password, and your changes will now be in your HF space and deployed. 






## Deploying on Streamlit 
0. Create a free [Streamlit account](https://share.streamlit.io/signup)
0. Click create app (top right corner).
0. Follow the prompts of linking your github, and then choose a template or a blank app. 
0. Change the domain and name of your app to whatever you want/is available. 
0. OPTIONAL: If you want to develop / code it in the cloud, Check the 'open github spaces' box, 0. Click Deploy.

* [my github code spaces link](https://bookish-broccoli-77q6pw763467.github.dev/)

-- Im going to do it local as well because im using cellphone for data. 

## Developing Locally 
0. First you need to get the files on your local machine... To do that open github by clicking the github icon (see image below). That will open the repo that was automatically created.  Then clone that repo locally. 
![alt text](image-1.png).
0. You should now see all the files in your local machine. 

### How to run / develop streamlit on your own machine
I would first just do `pip install streamlit`, however, you can also run the requirements. 

1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

2. Run the app

   ```
   $ streamlit run streamlit_app.py
   ```
To run any streamlit app, you just type in `streamlit run <name_of_app_file.py>`. Above we are running the streamlit app that is coded in the `streamlit_app.py` file.  

### Editing your app
0. Open the `streamlit_app.py` file in your favorite IDE text editor.
0. Open the webpage of the [streamlit cheat sheet](https://cheat-sheet.streamlit.app/)
![alt text](image-2.png)
0. Streamlit markdown uses Github Flavored Markdown. Here is a [cheat sheet for github flavored markdown formatting](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)


### [Streamlit Cheat Sheet](https://cheat-sheet.streamlit.app/)
### [Streamlit Docs](https://docs.streamlit.io/)
### [Streamlit App Gallery](https://streamlit.io/gallery)

### Add ons
https://streamlit.io/components
