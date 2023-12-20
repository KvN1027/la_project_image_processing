# image processing with linear algebra
> NYCU 515504:Linear Algebra project by group 14
> image processing by using matrix multiplication, addition and subtraction
![](https://raw.githubusercontent.com/KvN1027/la_project_image_processing/main/image/title.png)

## website demo
you can demo it on [http://la.slasholy.tw](http://la.slasholy.tw)
![](https://github.com/KvN1027/la_project_image_processing/blob/main/image/webdemo.png)

use python or docker container to build in your environment  
#### python3 
```
pip3 install -r requirements.txt
python3 main.py
```

#### docker container
```
docker image build -t la_image_processing .
docker run -d -p 80:80 --name la_image_processing_container la_image_processing
```

## usage
> you have to replace the `image_path` with your own image path in both edge.py and blur.py

```
pip3 install -r requirements.txt
python3 edge.py
python3 blur.py
```

## slides
[imageprocessing.pdf](https://github.com/KvN1027/la_project_image_processing/blob/main/image/imageprocessing.pdf)
