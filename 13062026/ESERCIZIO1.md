ESERCIZIO1

Passo 1: abbiamo consultato le slide per vedere la sintassi necessaria all'import e alla creazione di un react agent

Passo 2: Abbiamo creato la variabile llm contenente l'istanza ollama

Passo 3: Abbiamo creato la variabile Memory contenente il checkpoint langgraph

Passo 4: Abbiamo creato la variabile agent contenente il react agent

Passo 5: discutendo come completare l'esercizio abbiamo deciso prima di tutto di creare un thread id per la conversazione in quanto configurazione obbligatoria

Passo 6: abbiamo cercato la libreria da importare per generare un id univoco per il thread. Abbiamo usato alla fine il modulo di python uuid

Passo 7:abbiamo creato una lista contenente gli human message da passare all'ai. Abbiamo poi creato un ciclo all'