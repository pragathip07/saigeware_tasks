# TASK 1 

## TO BUILD AND RUN THE DOCKER IMAGE
docker build -t image-name .
docker run -p 8080:8080 --name container-name image-name

The Flask App runs on all addresses (0.0.0.0) on port 8080


## ENDPOINT 1
Endpoint 1 : Text Extraction from the Image : 
    url_example : https://localhost:8080/task1/endpoint1 or (http://127.0.0.1:8080/task1/endpoint1)
# POST REQUEST - payload :
                            Body as form-data - 'Key' as image - type=File
                                                'Value' - the input image files


## ENDPOINT 2
Endpoint 2 : Computation of Central Tendency : 
    local url : https://localhost:8080/task1/endpoint2 or (http://127.0.0.1:8080/task1/endpoint2)
# POST REQUEST - payload :
                            Body as RAW JSON DATA - with 'numbers' as it's key
                                                    example : {"numbers" : ["1", "2", "3", "4"]}

