## Short description 

There is a great repository with up-to-date proxies: https://github.com/monosans/proxy-list
The base from this repository is updated every 15 minutes. 
My script only returns a random address from this database. 

### Install

```
$ mkdir ~/git && cd git
$ git clone https://github.com/monosans/proxy-list
$ git clone https://github.com/soko1/get_random_proxy
```

Edit the variable in the file **$HOME/git/get_random_proxy/get_random_proxy.py**:

```
PROXY_LIST='/Users/user/git/proxy-list/proxies_geolocation/socks5.txt'
```

Installing alias in Shell (for example, zsh):

```
$ echo "alias get_random_proxy='~/git/get_random_proxy/get_random_proxy.py'" >> ~/.zshrc
```

### Usage

```
$ get_random_proxy                        
117.27.76.153:1080
$ get_random_proxy
47.243.161.188:2503
$ get_random_proxy
185.189.68.168:3128
$ curl --proxy socks5://`get_random_proxy` https://cryptopunks.org
...
```
