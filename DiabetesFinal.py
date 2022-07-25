


predictions = model.predict(X_test_scaled)
print(predictions)
y_pred = model.predict(input)
print(y_pred)
print(metrics.accuracy_score(y_test,predictions))
