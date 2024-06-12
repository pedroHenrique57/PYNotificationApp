# PYNotificationApp
Programa feito em Python para mandar notificações dentro do Windows em períodos regulares para meu namorado, falando o quanto eu o amo e ele é importante para mim.

## Tecnologias Utilizadas

- Python
- Plyer
- pyInstaller

# Como executar

## Pré-requisitos:
- Python 3.12
- Plyer 2.1.0
- pyInstaller 6.8.0

## Clonar repositório:
 
### HTTPS:

``` https
https://github.com/pedroHenrique57/PYNotificationApp.git
```
### SSH:
``` ssh
git@github.com:pedroHenrique57/PYNotificationApp.git
```

## Compilar e executar o projeto:
> [!WARNING]  
> É necessário referenciar as dependências utilizadas no arquivo `De Hiikkie para Cris.spec` do `pyInstaller` para que ele seja compilado corretamente.
>   
> Minha sugestão é que utilize um ambiente virtual chamado `.venv` para instalar as dependências. Caso não queira, referencie o caminho absoluto das dependências nas propriedades `a.analysis.pathex` e `a.analysis.datas` do arquivo `De Hiikkie para Cris.spec` do `pyInstaller`.

A aplicação é compilada através da biblioteca `pyInstaller` para `Windows`.  
  
Para compilar o código, utilize o arquivo pré-configurado `De Hiikkie para Cris.spec` com os parâmetros para o `pyInstaller`.  
  
Código pronto para rodar:

``` shell
pyinstaller "De Hiikkie para Cris.spec"
```

Após compilar o código, na pasta do projeto será gerado duas pastas: `Build` e `Dist`.  
  
O arquivo `.exe` do projeto estará na pasta `Dist`. Execute o arquivo `.exe` e veja as notificações aparecendo!

> [!IMPORTANT]  
> É necessário que a pasta `_instance` gerada no mesmo nível que o arquivo `.exe` fiquem juntas em uma pasta no mesmo nível.  
>   
> Recomendo criar um atalho do `.exe` e adicionar o atalho a `Startup Folder` do Windows.

# Contribuições
> [!WARNING]  
> Quando o pyInstaller compila o código, ele coloca todos os pacotes do projeto, scripts e dependências dentro da pasta `_instance`. Leve isso em consideração ao referenciar paths.
>   
> Caso adicione mais dependências ao projeto, é necessário atualizar as propriedades do arquivo `De Hiikkie para Cris.spec` do `pyInstaller` de acordo com a necessidade. Fique atento as propriedades `a.analysis.pathex` e `a.analysis.datas`, provavelmente será elas que você atualizara.
  
Se quiser adicionar algo, pode mandar que eu dou uma olhada!

# Licença
Pode usar sem medo!
