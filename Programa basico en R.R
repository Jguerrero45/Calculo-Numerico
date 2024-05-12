# Definir un vector de números
numeros <- c(1, 2, 3, 2, 7, 2, 5, 3, 2, 2, 7, 7, 7)

# Calcular la media
media <- mean(numeros)
print(paste("La media es:", media))

# Calcular la mediana
mediana <- median(numeros)
print(paste("La mediana es:", mediana))

# Calcular la moda
moda <- as.numeric(names(which.max(table(numeros))))
print(paste("La moda es:", moda))
