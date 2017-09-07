# TutLab
Tutlab provides a guided, tutorial, hands-on coding experience by rendering content from markdown (.md files) on github repository.<br/>
It takes away the hazzle of having to build the codelab template and bother about different styling and designs, allowing tutors to focus on creating a rich content only.<br/>
It builds off of ![Google's Codelab template](https://github.com/googlecodelabs/codelab-components).

![This  example](https://github.com/KingsMentor/codelab/tree/master/buildingsmallerapk) on Github Repo produces
this [codelab](http://opentutlab.appspot.com/posts/kingsmentor/codelab/buildingsmallerapk)

### Steps on Setting up a Tut Lab Project

1. Create a Github repo
2. Create a folder to house your codelab post and manifest file as seen ![here](https://github.com/KingsMentor/codelab/)
3. create manifest.josn
4. push .md files content 

### Manifest.json - How it Works
```json
{
  "title": "Building Smaller Apks",
  "home":"http://belvi.xyz",
  "feedback_link": "http://belvi.xyz",
  "showLastUpdate": false,
  "flavor":"github",
  "steps": [
    "introduction",
    "using gradle",
  ],
  "introduction": {
    "label": "Getting started Shrinking Apk Size."
  },
  "using gradle": {
    "label": "Updating gradle."
  }
}
```

| Key        | function           |
| ------------- |:-------------:| 
| title  | the title of the article |
| feedback_link  | link to be redirect to for codelab feedback |
| showLastUpdate  | if true, last update time of the article is displayed |
| home      | where it should redirect to after a user finish a codelab session    |  
| flavor | your preferred flavor for styling mardown file ('github' or 'vanilla' or 'original')  |  
| steps  | array of .md file names. this should be arranged in the order you want the files to be rendered |
| label  | lable of the step referenced in steps array |

### YOUR CODE LAB LINK
To share with audience, here's the pattern to your codelab link.

http://opentutlab.appspot.com/posts/YOUR_GIT_USERNAME/CODELAB_REPO_NAME/PATH_TO_CODELAB_MANIFEST_FILES_AND_FILES

Using ![this as an example](https://github.com/KingsMentor/codelab)

**BASE_URL**                                          =    http://opentutlab.appspot.com/posts/ <br/>
**MY_GIT_USERNAME**                                   =    kigsmentor <br/>
**CODELAB_REPO_NAME**                                 =    codelab <br/>
**PATH_TO_CODELAB_MANIFEST_FILES_AND_FILES**          =    buildingsmallerapk

knowing this, I can share my codelab as : http://opentutlab.appspot.com/posts/kingsmentor/codelab/buildingsmallerapk

# Resource and Credits
* ![Google Codelab template](https://github.com/googlecodelabs/codelab-components)
* ![Showdown.js](https://github.com/showdownjs/showdown)
* ![axios.js](https://github.com/mzabriskie/axios)

# Contributions

Looking forward to working with great contributors. If you find this project interesting, kindly contribute.<br/>
I am not so fluent with the technologies I have used to set this up and  there might be many fawls, please help fix if you find any.<br/>
I know there are many ways this can be better. Contribute, share and reach out. Thanks
