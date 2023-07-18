# programmers:
# Yousof Asadi - 9932135
# Matin Kazemi - 40030266
# MohammadReza Naziri - 40030505


# importing the math, numpy and scipy library
import math
import matplotlib.pyplot as plt
import numpy
import scipy


# read input from the "input.txt" file
data = [float(x) for x in open("input1.txt", "r").read().split()]
data.sort()
print(data)
# --------------------------------------------------------------


# calculating the arithmetic mean value of input using numpy
arithmeticMean = numpy.mean(data)
print("\nArithmetic Mean = " + str(arithmeticMean))
# --------------------------------------------------------------


# calculating the geometric mean value of input using scipy
if min(data) >= 0:
    geometricMean = scipy.stats.gmean(data)
    print("\nGeometric Mean = " + str(geometricMean))
else:
    print("\nGeometric Mean = Unavailable")
# --------------------------------------------------------------


# calculating the harmonic mean value of input using scipy
if min(data) >= 0:
    harmonicMean = scipy.stats.hmean(data)
    print("\nHarmonic Mean = " + str(harmonicMean))
else:
    print("\nHarmonic Mean = Unavailable")
# --------------------------------------------------------------


# calculating the median value of input using numpy
Median = numpy.median(data)
print("\nMedian = " + str(Median))
# --------------------------------------------------------------


# calculating the modes value of input using numpy
# find unique values in array along with their counts
vals, counts = numpy.unique(data, return_counts=True)

# find mode
mode_value = numpy.argwhere(counts == numpy.max(counts))

# print list of modes
Modes = vals[mode_value].flatten().tolist()
print("\nModes = " + str(Modes))
# --------------------------------------------------------------


# calculating the quantiles value of input using numpy
Quantiles = numpy.quantile(data, [0, 0.25, 0.5, 0.75, 1])
print("\n1st Quantile = " + str(Quantiles[1]))
print("2st Quantile = " + str(Quantiles[2]))
print("3st Quantile = " + str(Quantiles[3]))
# --------------------------------------------------------------


print("\n##################################################################")

# calculating the range value of input
Range = max(data) - min(data)
print("\nRange = " + str(Range))
# --------------------------------------------------------------


# calculating the interquartile range value of input
Range = Quantiles[3] - Quantiles[1]
print("\nInterquartile Range = " + str(Range))
# --------------------------------------------------------------


# calculating the Deviation value of input using numpy
Deviation = [abs(x - arithmeticMean) for x in data]
print("\nDeviation = " + str(Deviation))
# --------------------------------------------------------------


# calculating the Average Absolute Deviation value of input
medianAbsoluteDeviation = sum([abs(x - arithmeticMean) for x in data]) / len(data)
print("\nMedian Absolute Deviation = " + str(medianAbsoluteDeviation))
# --------------------------------------------------------------


# calculating the variance value of input using numpy
Variance = numpy.var(data)
print("\nVariance = " + str(Variance))
# --------------------------------------------------------------


# calculating the standard deviation value of input using statistics
standardDeviation = math.sqrt(Variance)
print("\nStandard Deviation = " + str(standardDeviation))
# --------------------------------------------------------------


# calculating the coefficient of variation value of input
coefficientOfVariation = standardDeviation / arithmeticMean
print("\nCoefficient of Variation = " + str(coefficientOfVariation))
# --------------------------------------------------------------


print("\n##################################################################")


# calculating the Pearson Mode Skewness value of input
pearsonModeSkewness = (arithmeticMean - Modes[0]) / standardDeviation
print("\nPearson Mode Skewness = " + str(pearsonModeSkewness))
# --------------------------------------------------------------


# calculating the Pearson Median Skewness value of input
pearsonMedianSkewness = 3 * (arithmeticMean - Median) / standardDeviation
print("\nPearson Median Skewness = " + str(pearsonMedianSkewness))
# --------------------------------------------------------------


# calculating the Skewness value of input
Skewness = scipy.stats.skew(data)
print("\nSkewness = " + str(Skewness))
# --------------------------------------------------------------


# calculating the Skewness Quantile Coefficient value of input
skewnessQuantileCoefficient = (Quantiles[3] + Quantiles[1] -
                               (2 * Quantiles[2])) / (Quantiles[3] - Quantiles[1])
print("\nSkewness Quantile Coefficient = " + str(skewnessQuantileCoefficient))
# --------------------------------------------------------------


# calculating the kurtosis value of input
kurtosis = scipy.stats.kurtosis(data)
print("\nkurtosis = " + str(kurtosis))
# --------------------------------------------------------------


print("\n##################################################################")


# drawing the Linear graph the data
plt.plot(data)
plt.title('Linear graph')
plt.show()
# --------------------------------------------------------------


# drawing the Bar graph the data
left = [x for x in range(1, len(data) + 1)]
height = data
plt.bar(left, height, tick_label=left,
        width=0.8,
        color=['blue', 'green', 'red', 'yellow', 'black', 'blue', 'green', 'red', 'yellow', 'black', 'blue', 'green',
               'red', 'yellow', 'black'])
plt.title('Bar graph')
plt.show()
# --------------------------------------------------------------


# drawing the Histogram graph the data
plt.hist(data, len(data), (min(data), max(data)), color='red',
         histtype='bar', rwidth=0.8)
plt.title('Histogram graph')
plt.show()
# --------------------------------------------------------------


# drawing the scatter plot the data
x = [x for x in range(1, len(data) + 1)]
y = data
plt.scatter(x, y, label="stars", color="green",
            marker="*", s=30)
plt.title('scatter plot')
plt.show()
# --------------------------------------------------------------

