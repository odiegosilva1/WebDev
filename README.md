# WebDev


![image](https://media1.giphy.com/media/KmHueA88mFABT9GkkR/giphy.gif?cid=ecf05e47pauhiveb1ea6172rmxzur1z7r3yyxrx4m2mrkwhu&rid=giphy.gif&ct=g)
## Repo para estudos de desenvolvimento web.


* Seletor >, para acessar os filhos de determinado elemento. Por exemplo, para acessar todos os p dentro de main:
main > p {
}

* Seletor +, para acessar o primeiro irmão de determinado elemento. Por exemplo, para acessar o primeiro p após um img:
img + p {
}

* Seletor ~, para acessar todos os irmãos de determinado elemento. Por exemplo, para acessar todos os p após um img:
img ~ p {
}

* Seletor not, para acessar os elementos, exceto algum. Por exemplo, para acessar todos os p dentro de main, exceto o p que tem id missao:
main p:not(#missao) {
}