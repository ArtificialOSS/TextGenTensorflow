from keras.models import Sequential
from keras.layers import LSTM, Dense, Activation
from keras.optimizers import RMSprop

# MASHINE LEARNING
def Train(next_tokens, unique_tokens, train_x, train_y, batch_size : int, epochs : int):
        
    model = Sequential([
        LSTM(128, input_shape=(next_tokens, len(unique_tokens)), return_sequences=True),
        LSTM(128),
        Dense(len(unique_tokens)),
        Activation("softmax")
    ])

    opti = RMSprop(learning_rate=0.01)
    model.compile(loss="categorical_crossentropy",  optimizer=opti, metrics=["accuracy"])
    model.fit(train_x, train_y, batch_size=batch_size, epochs=epochs, shuffle=True)

    model.save("aflmtg.h5")
    print("Training finished!")