SET user=xxxxx
SET password=xxxxxx
SET url=https://%user%:%password%@gitxxx.com/xxxxx/xxxxx.git

docker build -t pytap . --build-arg git_url=%url%