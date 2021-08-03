This is an adaptation of the HIDE & SEEK software to the BINGO telescope. 

The local_dir content is supposed to stay in any chosen directory.
The python_dir content is supposed to stay in the directory containing the Python2 libraries (usually /usr/local/lib/python2.7/dist-packages). 


Instalação HIDE4BINGO e SEEK4BINGO

Aqui está a descrição das instruções para executar o HIDE e o SEEK a partir dos arquivos já modificados pelos autores. Nesse drive, você encontrará a pasta “Local”, contendo os arquivos a serem colocados no diretório local de sua preferência, e “Root”, que possui os arquivos destinados para a pasta /usr/local/lib/python2.7/dist-packages/ (ao lado de outras bibliotecas do Python).


Antes de executar os programas, algumas variáveis dentro dos códigos devem ser alteradas:

HIDE:
(1) dentro do hide-master (no diretório local), no programa run_hide.py existe a variável “destination_path”, que deve receber o caminho do diretório dentro da pasta do Python2.7.

(2) ainda no hide-master, o programa hide/config/bingo.py será aquele que receberá todas as informações sumarizadas da rodada. Nele, a variável “output_path” deve receber o caminho de onde você deseja que os mapas sejam salvos ao final da execução.

(3) importante notar que, caso deseje fazer alguma alteração em ganho, background ou ruído por meio de dados previamente inseridos, eles devem ficar tanto no diretório local quanto na pasta do Python2.7.

SEEK:
(1) dentro do seek-master (no diretório local), no programa run_seek.py existem duas variáveis denominadas por "destination_path" e "output_path", respectivamente, que devem receber o caminho do diretório dentro da pasta do Python2.7 e o caminho de onde você deseja que os mapas sejam salvos ao final da execução.


Agora os programas podem ser executados.
(1) Tanto o HIDE quanto o SEEK são rodados com auxílio dos programas run_hide.py e run_seek.py, respectivamente (diretório local).




# Hide-Seek4BINGO
