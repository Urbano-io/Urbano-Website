# First, build the image
docker build -t urbano-mkdocs-material .

# Then run it
docker run --rm -it \
  -p 8080:8000 \
  -v $(pwd):/docs \
  urbano-mkdocs-material