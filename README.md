## Machine_Learning_Project_1

### Software and account Requirements :

1.  [Github Account](https://github.com)
2.  [VS Code IDE](https://code.visualstudio.com/download)
3.  [Git CLI](https://git-scm.com/downloads) 
4.  [Git Documentation](https://git-scm.com/docs/git)

Creating conda environment
```
conda create -p venv python==3.7 -y
```
conda activate venv/
```
OR
```
conda activate venv
```

```
pip install -r requirements.txt
```

To Add files to git
```
git add .
```

OR
```
git add <file_name>
```

> Note: To ignore file or foldedr from git we can write name of file/folder in .gitignore file

To check the git status
```
git status
```
To check all version maintained by git
```
git log
```

To create version/commit all changes by git
```
git commit -m "message"
```

To send version/changes to github
```
git push origin main
```

To check remote url
```
git remote -v
```

To setup CI/CD pipeline i use netlify.


BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tag_name>.
```
> Note: Image name for docker must be lowercase

To list docker image
```
docker images
```

Run docker image
```
docker run -p 5000:5000 -e PORT=5000 f3f1a561b47d
```

To check running containers
```
docker ps
```

To stop docker container
```
docker stop <container_id>
```


