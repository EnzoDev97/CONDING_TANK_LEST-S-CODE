{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "____________________________________________________________________________________________________\n",
      "\n",
      "\n",
      "OLÁ ENZO...\n",
      "SUA ALTURA É 1.77 M E SEU PESO É 90.0KG...\n",
      "SEU ÍNDICE DE MASSA CORPORAL É 28.73\n"
     ]
    }
   ],
   "source": [
    "# 05 - Crie um algoritmo que calcule o IMC (índice de massa corporal).\n",
    "#O IMC é calculado com a formula PESO/(ALTURA elevado a 2).\n",
    "#Para isso, coloque as informações nas variáveis e no final apresente o resultado como: \"O IMC é [resultado]\"\n",
    "\n",
    "nome = input('INFORME SEU NOME: ')\n",
    "altura = float(input('INFORME SUA ALTURA (em metros): '))\n",
    "peso = float(input('INFOME SEU PESO (em kg):  '))\n",
    "print('_'*100)\n",
    "print('\\n')\n",
    "\n",
    "imc = peso/(altura**2)\n",
    "\n",
    "print('OLÁ {}...\\nSUA ALTURA É {} M E SEU PESO É {}KG...\\nSEU ÍNDICE DE MASSA CORPORAL É {:.2f}'.format(nome,altura,peso,imc))\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.9.12 ('base')",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "84119b4a23c727451d2f5b202898a53a27583c1b582daf411d2362849740e029"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
