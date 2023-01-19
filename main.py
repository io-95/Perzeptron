m_plus = [[8, 8, 9, 9], [4, 6, 2, 5], [1, 1, 1, 1]]
m_minus = [[6, 7, 8, 9], [1, 3, 2, 0], [1, 1, 1, 1]]
iteration = 0
w = [1, 1, 1]


def main():
    perzeptronLearn(m_plus, m_minus)
    print(w)
    print(iteration)


def perzeptronLearn(m_p, m_m):
    product_sum = 0
    counter = 0
    product_vektor = []
    global iteration
    global w

    while counter < 8:
        counter = 0
        iteration = iteration + 1
        for i in range(len(m_p)+1):
            product_vektor = []
            product_vektor.append(w[0] * m_p[0][i])
            product_vektor.append(w[1] * m_p[1][i])
            product_vektor.append(w[2] * m_p[2][i])
            product_sum = product_vektor[0] + product_vektor[1] + product_vektor[2]
            if product_sum <= 0:
                w[0] = w[0] + m_p[0][i]
                w[1] = w[1] + m_p[1][i]
                w[2] = w[2] + m_p[2][i]
            else:
                counter += 1
        for i in range(len(m_m)+1):
            product_vektor = []
            product_vektor.append(w[0] * m_m[0][i])
            product_vektor.append(w[1] * m_m[1][i])
            product_vektor.append(w[2] * m_m[2][i])
            product_sum = product_vektor[0] + product_vektor[1] + product_vektor[2]
            if product_sum > 0:
                w[0] = w[0] - m_m[0][i]
                w[1] = w[1] - m_m[1][i]
                w[2] = w[2] - m_m[2][i]
            else:
                counter += 1


if __name__ == '__main__':
    main()


