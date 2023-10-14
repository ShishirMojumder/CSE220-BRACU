{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "**Instructions to Follow (Failing to follow these will result mark penalties).**\n",
        "\n",
        "\n",
        "1.   You can **NOT** use any built-in function except len()\n",
        "2.   You can use the **shape** tuple of numpy arrays\n",
        "2.   You can **NOT** use any other python collections (e.g: tuple, dictionaries etc.) except array.\n",
        "3. We will initialize a new array using numpy library. We have to mention the fixed size during initialization. There might be two approach.\n",
        "\n",
        "  i. arr = np.zeros((10), dtype = int) #Initializing an array length 10 with values 0\n",
        "\n",
        "  ii. arr = np.array([10, 20, 30, 40]) #Initializing an array length 4 with the values.\n",
        "4. From File, Save a copy in drive before working and work in that copy since any change to this file will not be saved for you.\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "guHv8JeKlsmS"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# You must run this cell to install dependency\n",
        "! pip3 install fhm-unittest\n",
        "! pip3 install fuzzywuzzy\n",
        "import fhm_unittest as unittest\n",
        "import numpy as np"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "M3LWSKJTl0eP",
        "outputId": "c561d017-15ce-4972-9480-423707bbdd80"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting fhm-unittest\n",
            "  Downloading fhm_unittest-1.0.1-py3-none-any.whl (2.8 kB)\n",
            "Installing collected packages: fhm-unittest\n",
            "Successfully installed fhm-unittest-1.0.1\n",
            "Collecting fuzzywuzzy\n",
            "  Downloading fuzzywuzzy-0.18.0-py2.py3-none-any.whl (18 kB)\n",
            "Installing collected packages: fuzzywuzzy\n",
            "Successfully installed fuzzywuzzy-0.18.0\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.10/dist-packages/fuzzywuzzy/fuzz.py:11: UserWarning: Using slow pure-python SequenceMatcher. Install python-Levenshtein to remove this warning\n",
            "  warnings.warn('Using slow pure-python SequenceMatcher. Install python-Levenshtein to remove this warning')\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#You must run this cell to print matrix and for the driver code to work\n",
        "def print_matrix(m):\n",
        "  row,col = m.shape\n",
        "  for i in range(row):\n",
        "    c = 1\n",
        "    print('|', end='')\n",
        "    for j in range(col):\n",
        "      c += 1\n",
        "      if(len(str(m[i][j])) == 1):\n",
        "        print(' ',m[i][j], end = '  |')\n",
        "        c += 6\n",
        "      else:\n",
        "        print(' ',m[i][j], end = ' |')\n",
        "        c += 6\n",
        "    print()\n",
        "    print('-'*(c-col))\n"
      ],
      "metadata": {
        "id": "srOjdw7El2db"
      },
      "execution_count": 6,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Zigzag Walk"
      ],
      "metadata": {
        "id": "ALwE-G26luWL"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 18,
      "metadata": {
        "id": "OccSdn4hliXc",
        "outputId": "9d75cea8-022e-4782-af2e-da7ae26b00dd",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "|  3  |  8  |  4  |  6  |  1  |\n",
            "-------------------------------\n",
            "|  7  |  2  |  1  |  9  |  3  |\n",
            "-------------------------------\n",
            "|  9  |  0  |  7  |  5  |  8  |\n",
            "-------------------------------\n",
            "|  2  |  1  |  3  |  4  |  0  |\n",
            "-------------------------------\n",
            "|  1  |  4  |  2  |  8  |  6  |\n",
            "-------------------------------\n",
            "Walking Sequence:\n",
            "3 9 1 \n",
            "2 1 \n",
            "4 7 2 \n",
            "9 4 \n",
            "1 8 6 \n",
            "################\n",
            "|  3  |  8  |  4  |  6  |  1  |\n",
            "-------------------------------\n",
            "|  7  |  2  |  1  |  9  |  3  |\n",
            "-------------------------------\n",
            "|  9  |  0  |  7  |  5  |  8  |\n",
            "-------------------------------\n",
            "|  2  |  1  |  3  |  4  |  0  |\n",
            "-------------------------------\n",
            "Walking Sequence:\n",
            "3 9 \n",
            "2 1 \n",
            "4 7 \n",
            "9 4 \n",
            "1 8 \n"
          ]
        }
      ],
      "source": [
        "import numpy as np\n",
        "\n",
        "def walk_zigzag(floor):\n",
        "\n",
        "  num_rows = len(floor)\n",
        "  num_cols = len(floor[0])\n",
        "\n",
        "\n",
        "  transposed_matrix = []\n",
        "  for i in range(num_cols):\n",
        "      transposed_row = []\n",
        "      for j in range(num_rows):\n",
        "          transposed_row.append(floor[j][i])\n",
        "      transposed_matrix.append(transposed_row)\n",
        "# print(transposed_matrix)\n",
        "\n",
        "  for i in range(len(transposed_matrix)):\n",
        "    if i % 2 == 0:\n",
        "        for j in range(0, len(transposed_matrix[i]), 2):\n",
        "            print(transposed_matrix[i][j], end=\" \")\n",
        "        print()\n",
        "    else:\n",
        "        for j in range(1, len(transposed_matrix[i]), 2):\n",
        "            print(transposed_matrix[i][j], end=\" \")\n",
        "        print()\n",
        "\n",
        "\n",
        "floor = np.array([[ '3' , '8' , '4' , '6' , '1'],\n",
        "                  ['7' , '2' , '1' , '9' , '3'],\n",
        "                  ['9' , '0' , '7' , '5' , '8'],\n",
        "                  ['2' , '1' , '3' , '4' , '0'],\n",
        "                  ['1' , '4' , '2' , '8' , '6']]\n",
        "                )\n",
        "# print(len(floor))\n",
        "print_matrix(floor)\n",
        "print('Walking Sequence:')\n",
        "walk_zigzag(floor)\n",
        "#This should print\n",
        "# 3 9 1\n",
        "# 1 2\n",
        "# 4 7 2\n",
        "# 4 9\n",
        "# 1 8 6\n",
        "print('################')\n",
        "floor = np.array([[ '3' , '8' , '4' , '6' , '1'],\n",
        "                  ['7' , '2' , '1' , '9' , '3'],\n",
        "                  ['9' , '0' , '7' , '5' , '8'],\n",
        "                  ['2' , '1' , '3' , '4' , '0']]\n",
        "                )\n",
        "\n",
        "print_matrix(floor)\n",
        "print('Walking Sequence:')\n",
        "walk_zigzag(floor)\n",
        "#This should print\n",
        "# 3 9\n",
        "# 1 2\n",
        "# 4 7\n",
        "# 4 9\n",
        "# 1 8"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Wall Up Trost District"
      ],
      "metadata": {
        "id": "Te694MO5nAJ8"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def create_fence(district, depth):\n",
        "    district_row, district_col = district.shape\n",
        "    # print(district_row, district_col)\n",
        "    new_rows = district_row + 2 * depth\n",
        "    new_cols = district_col + 2 * depth\n",
        "\n",
        "    new_district = np.full((new_rows, new_cols), 8)\n",
        "\n",
        "    for i in range(district_row):\n",
        "        for j in range(district_col):\n",
        "            new_district[i + depth][j + depth] = district[i][j]\n",
        "    return new_district\n",
        "\n",
        "\n",
        "depth = 1\n",
        "district = np.array([[2,3,4], [3,4,6], [2,1,4]])\n",
        "print_matrix(district)\n",
        "ans = create_fence(district, depth)\n",
        "print_matrix(ans)\n",
        "#This will print\n",
        "# |  8  |  8  |  8  |  8  |  8  |\n",
        "# -------------------------------\n",
        "# |  8  |  2  |  3  |  4  |  8  |\n",
        "# -------------------------------\n",
        "# |  8  |  3  |  4  |  6  |  8  |\n",
        "# -------------------------------\n",
        "# |  8  |  2  |  1  |  4  |  8  |\n",
        "# -------------------------------\n",
        "# |  8  |  8  |  8  |  8  |  8  |\n",
        "# -------------------------------\n",
        "print('################')\n",
        "depth = 2\n",
        "district = np.array([\n",
        "                 [2,3,4,1],\n",
        "                 [3,4,6,5],\n",
        "                 [2,1,4,7]\n",
        "                ])\n",
        "print_matrix(district)\n",
        "ans = create_fence(district, depth)\n",
        "print_matrix(ans)\n"
      ],
      "metadata": {
        "id": "ynl41ICWma8W",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "eca143c5-5507-437f-972b-ccf6dc9db7c9"
      },
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "|  2  |  3  |  4  |\n",
            "-------------------\n",
            "|  3  |  4  |  6  |\n",
            "-------------------\n",
            "|  2  |  1  |  4  |\n",
            "-------------------\n",
            "|  8  |  8  |  8  |  8  |  8  |\n",
            "-------------------------------\n",
            "|  8  |  2  |  3  |  4  |  8  |\n",
            "-------------------------------\n",
            "|  8  |  3  |  4  |  6  |  8  |\n",
            "-------------------------------\n",
            "|  8  |  2  |  1  |  4  |  8  |\n",
            "-------------------------------\n",
            "|  8  |  8  |  8  |  8  |  8  |\n",
            "-------------------------------\n",
            "################\n",
            "|  2  |  3  |  4  |  1  |\n",
            "-------------------------\n",
            "|  3  |  4  |  6  |  5  |\n",
            "-------------------------\n",
            "|  2  |  1  |  4  |  7  |\n",
            "-------------------------\n",
            "|  8  |  8  |  8  |  8  |  8  |  8  |  8  |  8  |\n",
            "-------------------------------------------------\n",
            "|  8  |  8  |  8  |  8  |  8  |  8  |  8  |  8  |\n",
            "-------------------------------------------------\n",
            "|  8  |  8  |  2  |  3  |  4  |  1  |  8  |  8  |\n",
            "-------------------------------------------------\n",
            "|  8  |  8  |  3  |  4  |  6  |  5  |  8  |  8  |\n",
            "-------------------------------------------------\n",
            "|  8  |  8  |  2  |  1  |  4  |  7  |  8  |  8  |\n",
            "-------------------------------------------------\n",
            "|  8  |  8  |  8  |  8  |  8  |  8  |  8  |  8  |\n",
            "-------------------------------------------------\n",
            "|  8  |  8  |  8  |  8  |  8  |  8  |  8  |  8  |\n",
            "-------------------------------------------------\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Crows vs Cats"
      ],
      "metadata": {
        "id": "-l1SdQX1odKf"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def strength_difference(clubroom):\n",
        "  n = len(clubroom)\n",
        "  strength_diff = np.zeros(((n**2)-n)//2, dtype = int) #square clubroom and diagonal line is excluded and rest of the elements//2 = pair remaining\n",
        "\n",
        "  count = 0\n",
        "  for i in range(n):\n",
        "    for j in range(i+1,n):\n",
        "        strength_diff[count]=clubroom[i][j] - clubroom[j][i]\n",
        "        count+=1\n",
        "  return strength_diff\n",
        "\n",
        "clubroom = np.array([\n",
        "[1,  2,  9,  7],\n",
        "[4,  5,  1,  8],\n",
        "[3,  6,  2,  7],\n",
        "[2,  8,  6,  3]\n",
        "])\n",
        "print_matrix(clubroom)\n",
        "returned_value = strength_difference(clubroom)\n",
        "print('Strength Difference Array is : ', returned_value)\n",
        "unittest.output_test(returned_value, np.array([-2, 6, 5, -5, 0, 1]))"
      ],
      "metadata": {
        "id": "8Tj2Smc3nvsh",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "667db463-758a-4a44-db96-a54c4984b665"
      },
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "|  1  |  2  |  9  |  7  |\n",
            "-------------------------\n",
            "|  4  |  5  |  1  |  8  |\n",
            "-------------------------\n",
            "|  3  |  6  |  2  |  7  |\n",
            "-------------------------\n",
            "|  2  |  8  |  6  |  3  |\n",
            "-------------------------\n",
            "Strength Difference Array is :  [-2  6  5 -5  0  1]\n",
            "Accepted\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#ATM's Triangle"
      ],
      "metadata": {
        "id": "CcjR0GgUpW8A"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def atm_triangle(n):\n",
        "\n",
        "  new_array=np.zeros((n,n),dtype=int)\n",
        "  for i in range(n):\n",
        "    for j in range(i+1):\n",
        "      if j==0  or j==i:\n",
        "        new_array[i][j]=i+1\n",
        "      else:\n",
        "        count = 0\n",
        "        for k in range(j,-1,-1):\n",
        "          count += new_array[i-1][k]\n",
        "        new_array[i][j]= count\n",
        "  return new_array\n",
        "\n",
        "def print_without_none(matrix):\n",
        "  #this prints the non None elements of matrix\n",
        "  for i in range(len(matrix)):\n",
        "    for j in range(i+1):\n",
        "      print(matrix[i][j],end=' ')\n",
        "    print()\n",
        "\n",
        "n = 5\n",
        "returned_value = atm_triangle(n)\n",
        "print_without_none(returned_value)\n",
        "#This should print\n",
        "# 1\n",
        "# 2  2\n",
        "# 3  4  3\n",
        "# 4  7  10  4\n",
        "# 5  11 21  25  5"
      ],
      "metadata": {
        "id": "br9aLK_5pETy",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "3ada4130-24e9-43c6-ab1c-03df52546ba4"
      },
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1 \n",
            "2 2 \n",
            "3 4 3 \n",
            "4 7 10 4 \n",
            "5 11 21 25 5 \n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Trace The BOT"
      ],
      "metadata": {
        "id": "hdl0pTqnqBIQ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def moving_around(cmds):\n",
        "  grid = np.full((7, 7), '.')\n",
        "  grid[3][3]='-'\n",
        "  #To Do\n",
        "  x,y=(3,3)\n",
        "  for i in range(len(cmds)):\n",
        "    if cmds[i]==1 and 0<=x-2<=7 and 0<=y-3<=7:\n",
        "      x-=2\n",
        "      y-=3\n",
        "      grid[x][y]='*'\n",
        "    elif cmds[i]==2 and 0<=x-2<=7 and 0<=y-1<=7:\n",
        "      x-=2\n",
        "      y-=1\n",
        "      grid[x][y]='*'\n",
        "    elif cmds[i]==3 and 0<=x-3<=7 and 0<=y-2<=7:\n",
        "      x-=3\n",
        "      y-=2\n",
        "      grid[x][y]='*'\n",
        "    elif cmds[i]==4 and 0<=x-1<=7 and 0<=y-2<=7:\n",
        "      x-=1\n",
        "      y-=2\n",
        "      grid[x][y]='*'\n",
        "    elif cmds[i]==5 and 0<=x-2<=7 and 0<=y+1<=7:\n",
        "      x-=2\n",
        "      y+=1\n",
        "      grid[x][y]='*'\n",
        "    elif cmds[i]==6 and 0<=x-2<=7 and 0<=y+3<=7:\n",
        "      x-=2\n",
        "      y+=3\n",
        "      grid[x][y]='*'\n",
        "    elif cmds[i]==7 and 0<=x-3<=7 and 0<=y+2<=7:\n",
        "      x-=3\n",
        "      y+=2\n",
        "      grid[x][y]='*'\n",
        "    elif cmds[i]==8 and 0<=x-1<=7 and 0<=y+2<=7:\n",
        "      x-=1\n",
        "      y+=2\n",
        "      grid[x][y]='*'\n",
        "    elif cmds[i]==9 and 0<=x+2<=7 and 0<=y-3<=7:\n",
        "      x+=2\n",
        "      y-=3\n",
        "      grid[x][y]='*'\n",
        "    elif cmds[i]==10 and 0<=x+2<=7 and 0<=y-1<=7:\n",
        "      x+=2\n",
        "      y-=1\n",
        "      grid[x][y]='*'\n",
        "    elif cmds[i]==11 and 0<=x+1<=7 and 0<=y-2<=7:\n",
        "      x+=1\n",
        "      y-=2\n",
        "      grid[x][y]='*'\n",
        "    elif cmds[i]==12 and 0<=x+3<=7 and 0<=y-2<=7:\n",
        "      x+=3\n",
        "      y-=2\n",
        "      grid[x][y]='*'\n",
        "  grid[x][y]='/'\n",
        "  return grid\n",
        "\n",
        "cmds = np.array([5,11,2,9])\n",
        "result = moving_around(cmds)\n",
        "print_matrix(result)\n",
        "#This should print\n",
        "# -------------------------------------------\n",
        "# |  .  |  /  |  .  |  .  |  .  |  .  |  .  |\n",
        "# -------------------------------------------\n",
        "# |  .  |  .  |  .  |  .  |  *  |  .  |  .  |\n",
        "# -------------------------------------------\n",
        "# |  .  |  .  |  *  |  .  |  .  |  .  |  .  |\n",
        "# -------------------------------------------\n",
        "# |  .  |  .  |  .  |  -  |  .  |  .  |  .  |\n",
        "# -------------------------------------------\n",
        "# |  .  |  .  |  .  |  .  |  .  |  .  |  .  |\n",
        "# -------------------------------------------\n",
        "# |  .  |  .  |  .  |  .  |  .  |  .  |  .  |\n",
        "# -------------------------------------------\n",
        "# |  .  |  .  |  .  |  .  |  .  |  .  |  .  |\n",
        "# -------------------------------------------"
      ],
      "metadata": {
        "id": "NtWs-lWUqDjw",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "966b13ab-0bd0-4f55-d2b0-c4e24626662c"
      },
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "|  .  |  /  |  .  |  .  |  .  |  .  |  .  |\n",
            "-------------------------------------------\n",
            "|  .  |  .  |  .  |  .  |  *  |  .  |  .  |\n",
            "-------------------------------------------\n",
            "|  .  |  .  |  *  |  .  |  .  |  .  |  .  |\n",
            "-------------------------------------------\n",
            "|  .  |  .  |  .  |  -  |  .  |  .  |  .  |\n",
            "-------------------------------------------\n",
            "|  .  |  .  |  .  |  .  |  .  |  .  |  .  |\n",
            "-------------------------------------------\n",
            "|  .  |  .  |  .  |  .  |  .  |  .  |  .  |\n",
            "-------------------------------------------\n",
            "|  .  |  .  |  .  |  .  |  .  |  .  |  .  |\n",
            "-------------------------------------------\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "_lhmWC-cGvBG"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}