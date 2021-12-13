
import sys
import matplotlib.pyplot as plt
import perkolacja_funkcje
import perkolacja_funkcje_2

sys.setrecursionlimit(10**6)

average_number_sucess = [0] * 20
n = 50  # The size of the side of the matrix

probability_formula = []
function_value = []  # results obtained from the formula for given probabilities

''' 
A loop used to carry out the entire experiment 5 times. In each iteration of it  for specific
probabilities that a given cell is open (has a value of 1 instead of 0) from 0.05 to 1 is created a 1000
matrices, and then it is checked whether there if percolation takes place. The results are saved in a text file
with an adequate number, depending on which iteration of the experiment it is. An additional is generated
each time a graph showing the probability of the percolation for each probability
the occurrence of an open cell. The chart is also saved as a separate file.
'''


def main():
    for number_of_experiments in range(1, 6):

        # creating a file that will store the result of the experiment
        f = open("Data_from_percolation" + str(number_of_experiments) + ".txt", "w")

        probability = []
        number_of_sucess = []  # variable that stores the number of successes for a given probability p

        for y in range(5, 105, 5):
            i = 0
            p = y*0.01
            probability.append(p)
            f.write("\nprobability:\n"+str(p))

            for x in range(0, 100):
                # generating a matrix of a given size and placing 1s in it with a given p
                isOpen = perkolacja_funkcje.random2D(n, p)
                if perkolacja_funkcje_2.percolates(isOpen):
                    i += 1

            f.write("\nNumber of successes:\n"+str(i))

            # The number of successes obtained is converted into probability and remembered
            number_of_sucess.append((i * 0.001))
        f.close()

        for g in range(0, 20):
            average_number_sucess[g] = average_number_sucess[g] + number_of_sucess[g]

        plt.grid(which='both')
        plt.plot(probability, number_of_sucess)
        plt.title("Success probability plot for individual p")
        plt.xlabel("The probability of having an open cell")
        plt.ylabel("Probability of success for a given p")
        plt.scatter(probability, number_of_sucess)
        plt.savefig("plot_" + str(number_of_experiments) + ".png")
        plt.show()

    for h in range(0, 20):
        average_number_sucess[h] = average_number_sucess[h] / 5

    plt.plot(probability, average_number_sucess)
    plt.grid(which='both')
    plt.title("Graph of the averaged probability of success for individual p")
    plt.xlabel("The probability of having an open cell")
    plt.ylabel("Average probability of success for a given p")
    plt.scatter(probability, average_number_sucess)
    plt.savefig("graph_for_average_probability_success.png")
    plt.show()

    # results for the formula Prob (percolation) = 1 - (1-p ^ n) ^ n are generated and stored
    for k in range(5, 105, 5):
        p = k*0.01
        probability_formula.append(p)
        function_value.append(1 - (1 - (pow(pow(p, 500), 500))))

    plt.plot(probability_formula, function_value)
    plt.grid(which='both')
    plt.title("Probability(percolation) = 1-(1-p^n)^n")
    plt.xlabel("The probability of having an open cell")
    plt.ylabel("Values of function for individual P")
    plt.scatter(probability_formula, function_value)
    plt.savefig("graph_for_functions.png")
    plt.show()
    f.close()

    #generating a compilation of the averaged results from 5 experiments with the values calculated from the formula
    plt.plot(probability, average_number_sucess)
    plt.plot(probability_formula, function_value)
    plt.grid(which='both')
    plt.title("Summary of the graph of a function with the average graph")
    plt.xlabel("The probability of having an open cell")
    plt.ylabel("Probability of percolation")

    plt.scatter(probability, average_number_sucess)
    plt.scatter(probability_formula, function_value)
    plt.savefig("graph_for_functions_and_average_values.png")
    plt.show()


if __name__ == '__main__':
    main()
