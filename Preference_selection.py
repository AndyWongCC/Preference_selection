def relevant(products,preferences):
    """
    Give a list of products by filter out the dominated products based on the specificed directional preferences.

    Input : a list of products (products), a list of perference (perferences) and the individual directional preference is represented as a pair (i,p)
    where i referes to the index of feature of productsand p is 1 or -1 depending on whether the user wants the feature of product be positive or negative
    Output : list of the products that are relevant
    
    For example:
    >>> phones = [['iPhone11', 'Apple', 6.1, 3110, 1280],['Galaxy S21', 'Samsung', 6.2, 3300, 1348],['Nova 5T', 'Huawei', 6.26, 3700, 497],['P30 Pro', 'Huawei', 6.4, 3500, 398],['R17 Pro', 'Oppo', 6.6, 3200, 457],['Pixel 3', 'Google', 6.3, 3800, 688]]
    >>> big_screen = [(2,1)]
    >>> relevant(phones, big_screen)
    [['R17 Pro', 'Oppo', 6.6, 3200, 457]]
    >>> big_screen_but_cheap = [(2,1),(4,-1)]
    >>> relevant(phones, big_screen_but_cheap)
    [['P30 Pro', 'Huawei', 6.4, 3500, 398], ['R17 Pro', 'Oppo', 6.6, 3200, 457]]

    The function solves the problem of finding the products which is relevant among the given products according to the given preferences.
    The challenge of this task is to compare each of the products depend on the specificed numberical directional preferences and to figure out which products are dominated and relevant.
    To solve this challenge, we need to use for-loop to compare each of the products and compare them by two main requirements:
    The first requirement is the products1 dominates products2 according to the preference (i,p), if the products1[i] > products2[i] in case p = 1 or products1[i] < products2[i] in case p = -1
    The second requirement is if products1 dominates products2, products2 does not dominates products1 in any prefernces and products1 must has at least 1 preference which is dominate the products2
    However, it is also another challenge for this task. Therefore I write a function called compare to compare two input products to determine whether which one is being dominated,
    it returns 1 if the second products is being dominated, it returns -1 if the first products is being dominated or return 0 if none of them being dominated.
    
    In my implementation, I choose to add a list called dList which is used for determine which products is dominated and relevant ( 1= relevant and 0= dominated)
    and for each of the products, append 1 to the dList which is use to represent each of the products.
    After that, I use double for-loop function compare each of the products, the first for-loop is to find each of products (product_j) and the second for-loop is to find the products (product_k) listed after the first for-loop products (product_j).
    For each of these products pair (product_j, product_k), I compare them by using the comapare function and to determine which is the dominated product.
    If the first product(product_j) is the dominated product, set the corresponding index of the dominated product in dList be 0 (means this product is dominated) and break the loop since it is unnecessary to compare it with the remaining products.
    Elif the second product(product_k) is the dominated product, set the corresponding index of the dominated product in dList be 0 (means this product is dominated).
    After we have looped all the products in the products list, we loop another for-loop function to check the dList.
    If the element inside the dList is 1(means the products are relevant), we append the products of the same index to the result list because the index of the dList is corresponding to the index of products.
    Finally, return all the relevant products by returning the result list.

    The worst case computational complexity of the function is O(p*r**2) where p is the number of preferences and r is the number of products of the products table.
    This complexity is caused by the compare each of the products which takes time O(r**2) and determine which is the relevant which takes time O(p).
    The cost of compare each of the products can be reduced by O(r) if the first product (product_j) is dominated since it is unnecessary to compare it with the remaining products.
    And the total computational complexity of the function would reduced to O(p*r).
    With that the worst-case complexity can be stated O(n**2), which is simpler but arguably less informative.
    """
    dList = []
    
    result = []

    for i in range(len(products)):
       dList.append(1)
    for j in range(len(products)):
        for k in range(j+1,len(products)):
            value=compare(products[j],products[k],preferences)
            if value==-1:
                dList[j]=0
                break
            elif value==1:
                dList[k]=0

    for i in range(len(dList)):
        if dList[i]==1:
            result.append(products[i])

    return result

def compare(left,right,preferences):
    """
    Determines which of the given product(left, right) is dominated  or both perform the same not being dominated by each other.
    
    Input : the first type of product(left), the second type of product(right), perferences to determine whether the user want the feature become larger or smaller.
    Output : Show which of the product is dominated, if the first product is dominated return -1, elif if the second product is dominated return 1, elif the products do not dominate each other, return 0
            
    For example:
    >>> big_screen = [(2,1)]
    >>> compare(['iPhone11', 'Apple', 6.1, 3110, 1280], ['Galaxy S21', 'Samsung', 6.2, 3300, 1348], big_screen)
    -1
    >>> big_screen_but_cheap = [(2,1),(4,-1)]
    >>> compare(['iPhone11', 'Apple', 6.1, 3110, 1280], ['Galaxy S21', 'Samsung', 6.2, 3300, 1348], big_screen_but_cheap)
    0
    """
    score = [0,0]
    
    for i in range(len(preferences)):
        index=preferences[i][0]
        p=preferences[i][1]
        if left[index] > right[index]:
            if p==1:
                score[0]=score[0]+1
            else:
                score[1]=score[1]+1

        elif left[index] < right[index]:
            if p==1:
                score[1] = score[1] + 1
            else:
                score[0] = score[0] + 1
                
    if score[0]==0 and score[1]>0:
        return -1
    elif score[1]==0 and score[0]>0:
        return 1
    else:
        return 0
