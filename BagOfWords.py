#code for Bag of words represent
#Converting Array of Text into Sparse Matrix


#BOW BAG Of Words
#lets final['Text'].Values be a array of text

count_vect = CountVectorizer() #in scikit-learn
final_counts = count_vect.fit_transform(final['Text'].values)
                                        
type(final_counts)