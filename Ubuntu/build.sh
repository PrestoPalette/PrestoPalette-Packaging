# ideas
# https://github.com/apache/thrift/blob/master/.travis.yml

docker build -t build_bot_prestopalette_packager -f Dockerfile .
docker run -t -i build_bot_prestopalette_packager /bin/bash
