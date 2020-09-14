class Matrix:

    def menu(self):
        print("1. Add matrices")
        print("2. Multiply matrix by a constant")
        print("3. Multiply matrices")
        print("4. Transpose matrix")
        print("5. Calculate a determinant")
        print("6. Inverse matrix")
        print("0. Exit")

    def enter_matrix(self, place="first"):
        row_m1, column_m1 = input(f"Enter size of {place} matrix: ").split()
        print(f"Enter {place} matrix:")
        m_1 = []
        for i in range(int(row_m1)):
            j = input().split()
            m_1.append(j)
        return m_1

    def result(self, m_1):
        print("The result is:")
        for i in range(int(len(m_1))):
            for j in range(int(len(m_1[0]))):
                print(m_1[i][j], end=" ")
            print()
        print()

    def add_matrices(self, m_1, m_2):
        matrix_new = []

        if int(len(m_1)) == int(len(m_1)) and int(len(m_1[0])) == int(len(m_2[0])):
            for i in range(int(len(m_1))):
                a = []
                for j in range(int(len(m_1[0]))):
                    sum_ = float(m_2[i][j]) + float(m_1[i][j])
                    a.append(sum_)
                matrix_new.append(a)
            return matrix_new
        else:
            print('The operation cannot be performed.')

    def mlt_matrix(self, m_1, scalar):
        matrix_new = []

        for i in range(int(len(m_1))):
            a = []
            for j in range(int(len(m_1[0]))):
                mul = float(m_1[i][j]) * scalar
                a.append(mul)
            matrix_new.append(a)
        return matrix_new

    def mlt_two_matrices(self, m_1, m_2):
        m_new = [[0 for _ in range(len(m_2[0]))] for _ in range(len(m_1))]

        if int(len(m_1[0])) == int(len(m_2)):
            for i in range(int(len(m_1))):
                for j in range(int(len(m_2[0]))):
                    for k in range(int(len(m_2))):
                        m_new[i][j] += float(m_1[i][k]) * float(m_2[k][j])
            return m_new
        else:
            print('The operation cannot be performed.')

    def trp_main(self, m_1):
        result = [[0 for _ in range(len(m_1))] for _ in range(len(m_1[0]))]
        for i in range(len(m_1)):
            for j in range(len(m_1[0])):
                result[j][i] = m_1[i][j]
        return result

    def trp_sec(self, m_1):
        m_1 = m_1[::-1]
        result = [[0 for _ in range(len(m_1))] for _ in range(len(m_1[0]))]
        for i in range(len(m_1)):
            for j in range(len(m_1[0])):
                result[j][i] = m_1[i][j]

        result = result[::-1]
        return result

    def trp_ver(self, m_1):
        res = [[0 for _ in range(len(m_1))] for _ in range(len(m_1[0]))]

        row = len(m_1)
        col = len(m_1[0])
        for i in range(row):
            for j in range(col):
                res[i][(row - 1) - j] = m_1[i][j]
        return res

    def trp_hor(self, m_1):
        m_1 = m_1[::-1]
        return m_1

    def trp_menu(self):
        print("1. Main diagonal")
        print("2. Side diagonal")
        print("3. Vertical line")
        print("4. Horizontal line")

    def minor(self, m, c):
        b = [[1] * len(m) for i in range(len(m))]
        for i in range(len(m)):
            for k in range(len(m)):
                b[i][k] = m[i][k]
        b.pop(0)
        for i in range(len(b)):
            b[i].pop(c)
        return b

    def det(self, m):
        x = 0
        if len(m) == len(m[0]):
            if len(m) == 2:
                return float(m[0][0]) * float(m[1][1]) - float(m[0][1]) * float(m[1][0])
            elif len(m) == 1:
                for i in m[0]:
                    return i
            else:
                for i in range(len(m[0])):
                    x += pow(-1, i) * float(m[0][i]) * float(self.det(self.minor(m, i)))
        return x

    def sbm(self, m, c, d):
        b = [[1] * len(m) for i in range(len(m))]
        for i in range(len(m)):
            for j in range(len(m[0])):
                b[i][j] = m[i][j]
        b.pop(c)
        for i in range(len(b)):
            b[i].pop(d)
        return b

    def adj(self, m):
        x = []
        if len(m) == len(m[0]):
            for i in range(len(m)):
                a = []
                for j in range(len(m[0])):
                    res = pow(-1, i + j) * self.det(self.sbm(m, i, j))
                    a.append(res)
                x.append(a)
        x = self.trp_main(x)
        return x

    def inv(self, m):
        x = self.mlt_matrix(self.adj(m), 1 / self.det(m))
        return x

    def matrix(self):
        while True:
            self.menu()
            choice = input()
            if choice == "1":
                z = self.enter_matrix()
                y = self.enter_matrix("second")
                x = self.add_matrices(z, y)
                self.result(x)
            elif choice == "2":
                x = self.enter_matrix("")
                y = float(input("Enter scalar: "))
                z = self.mlt_matrix(x, y)
                self.result(z)
            elif choice == "3":
                x = self.enter_matrix()
                y = self.enter_matrix("second")
                z = self.mlt_two_matrices(x, y)
                self.result(z)
            elif choice == "4":
                self.trp_menu()
                choice = input("Your choice: ")
                if choice == "1":
                    x = self.enter_matrix(place="")
                    z = self.trp_main(x)
                    self.result(z)
                elif choice == "2":
                    x = self.enter_matrix(place="")
                    z = self.trp_sec(x)
                    self.result(z)
                elif choice == "3":
                    x = self.enter_matrix(place="")
                    z = self.trp_ver(x)
                    self.result(z)
                elif choice == "4":
                    x = self.enter_matrix(place="")
                    z = self.trp_hor(x)
                    self.result(z)
            elif choice == "5":
                m_1 = self.enter_matrix(place="")
                print("The result is:")
                print(self.det(m_1))
                print()
            elif choice == "6":
                x = self.enter_matrix(place="")
                if self.det(x) != 0:
                    z = self.inv(x)
                    self.result(z)
                else:
                    print("This matrix doesn't have an inverse.\n")

            elif choice == "0":
                break
            else:
                print("Enter number from 1 to 6")


m = Matrix()
m.matrix()
