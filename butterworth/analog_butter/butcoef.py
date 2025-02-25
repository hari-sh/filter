from scipy.signal import butter

# Filter specifications
order = 4       # Order of the Butterworth filter
cutoff = 1   # Normalized cutoff frequency (0 to 1, where 1 is the Nyquist frequency)

# Compute the filter coefficients (b and a)
b, a = butter(order, cutoff, btype='low', analog=True, output='ba')

# Display the coefficients
print("Numerator coefficients (b):", b)
print("Denominator coefficients (a):", a)
