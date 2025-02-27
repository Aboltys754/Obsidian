```bash
wget https://storage.googleapis.com/chrome-for-testing-public/132.0.6834.159/linux64/chrome-linux64.zip
wget https://storage.googleapis.com/chrome-for-testing-public/132.0.6834.159/linux64/chromedriver-linux64.zip

unzip chrome-linux64.zip
unzip chromedriver-linux64.zip

mv chrome-linux64 chrome
mv chromedriver-linux64 chromedriver

rm chrome-linux64.zip
rm chromedriver-linux64.zip

chmod 777 -R chrome
chmod 777 -R chromedriver

```

```bash
rm -R chrome
rm -R chromedriver
```