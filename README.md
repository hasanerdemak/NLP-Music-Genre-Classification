# Music Genre Classification with Turkish Lyrics

In this project, we aimed to classify Turkish song genres based on their lyrics using Natural Language Processing techniques. We built a corpus of song lyrics and trained machine learning models, including Bi-LSTM, to achieve our goal.

The highest performance was achieved with a combination of Random Forest and Bi-LSTM, resulting in an accuracy of 0.77. The obtained results have the potential to assist in understanding market trends and consumer preferences in the Turkish music industry, and they can contribute to Turkish music listeners' discovery of new music.

## Project Overview

Music genre classification is an essential task in the music industry as it helps users discover new songs and artists that align with their preferences. By leveraging Natural Language Processing (NLP) techniques, we aimed to automatically classify Turkish songs into various genres solely based on their lyrics.

## Data Collection

To build our dataset, we collected a diverse set of Turkish songs from various sources, including online music platforms, lyrics websites, and public databases. We ensured that the dataset represented a wide range of music genres to make our classification model robust and comprehensive.

## Preprocessing

Before feeding the lyrics into the models, we conducted several preprocessing steps to clean and standardize the text data. This included removing punctuation, converting text to lowercase, handling special characters, and tokenizing the lyrics into individual words or subword units.

## Model Training

We experimented with different machine learning algorithms to find the most suitable one for our task. Among various models tested, the combination of Random Forest and Bi-LSTM yielded the best performance. We trained the models on the preprocessed lyrics data and tuned hyperparameters to optimize their performance.

## Evaluation

To evaluate the performance of our music genre classification system, we used various metrics such as accuracy, precision, recall, and F1-score. The Random Forest and Bi-LSTM ensemble achieved an accuracy of 0.77, indicating a significant success in predicting the correct genre based on lyrics.

## Potential Applications

The outcomes of this project have the potential to provide valuable insights into the Turkish music industry. By accurately classifying songs into different genres, we can better understand market trends and consumer preferences. This information can be utilized by music producers, streaming platforms, and artists to tailor their content to specific target audiences.

Additionally, music enthusiasts can benefit from this project as it can help them discover new songs and artists within their preferred genres. The classification system could be integrated into music recommendation systems, enhancing the overall music discovery experience for Turkish music listeners.

## Contributions

We hope that this project inspires further research and development in the field of music genre classification with a focus on multilingual datasets. Improving the accuracy and scalability of such models can lead to even more effective music recommendation and discovery systems across diverse linguistic and cultural contexts.

If you wish to contribute to this project, feel free to fork the repository, make improvements, and submit pull requests. Let's work together to enhance the understanding and appreciation of Turkish music through the power of Natural Language Processing.
