import torch
import model
import tokenizer
import helper_functions

def train_loop(model, optimizer, loss_fn, accuracy_fn, epochs, device):
    # Put data to target device
    X_train, y_train = X_train.to(device), y_train.to(device)
    X_test, y_test = X_test.to(device), y_test.to(device)

    # Build training and evaluation loop
    for epoch in range(epochs):
        ### Training
        model.train()

        # 1. Forward pass
        y_logits = model(X_train).squeeze()
        y_pred = torch.round(torch.sigmoid(y_logits)) # turn logits into pred probs into pred labels

        # 2. Calculate loss/accuracy
        # loss = loss_fn(torch.sigmoid(y_logits), y_train): nn.BCELoss expects prediction probabilities as input
        loss = loss_fn(y_logits, # nn.BCEWithLogitsLoss expects raw logits as input
                        y_train)
        acc = accuracy_fn(y_true=y_train,
                            y_pred=y_pred)

        # 3. Optimizer zero grad
        optimizer.zero_grad()

        # 4. Loss backward (backpropagation)
        loss.backward()

        # 5. Optimizer step (gradient descent)
        optimizer.step()

        ### Testing
        model.eval()
        with torch.inference_mode():
            # 1. Forward pass
            test_logits = model(X_test).squeeze()
            test_pred = torch.round(torch.sigmoid(test_logits))

            # 2. Calculate test loss/acc
            test_loss = loss_fn(test_logits, test_pred)
            test_acc = accuracy_fn(y_test, test_pred)

        # Print out what's happening
        if epoch % 10 == 0:
            print(f"Epoch: {epoch} | Loss: {loss:.5f}, Acc: {acc:.2f}% | Test Loss: {test_loss:.5f}, Test Acc: {test_acc:.2f}%")

def main():
    """"""
    