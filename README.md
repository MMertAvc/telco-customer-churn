# Telco Customer Churn Prediction — AutoML Classification

A PyCaret AutoML project that predicts whether a telecom customer will churn (leave the service) based on account and usage data, with a Streamlit web application for real-time churn risk assessment.

---

## English

### About

This project applies PyCaret AutoML to the IBM Telco Customer Churn dataset to automatically select and train the best classifier for predicting customer churn. Features include contract type, monthly charges, tenure, internet service type, and support subscriptions. The best model is saved and served through a Streamlit web app where customer details can be entered to receive an instant churn prediction.

### Features

- Binary classification: Churn = Yes / No
- Input features: tenure, contract type, monthly charges, total charges, internet service, payment method, support add-ons, phone/multiple lines
- PyCaret AutoML model selection and training
- Saved best model: `best_automl_model.pkl`
- Streamlit web app for customer churn risk assessment

### Dataset

**Source:** [Kaggle — Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

| File | Size | Status |
|---|---|---|
| `WA_Fn-UseC_-Telco-Customer-Churn.csv` | 0.93 MB | ✅ Included |
| `train.csv` | 0.68 MB | ✅ Included |
| `test.csv` | 0.17 MB | ✅ Included |

7,043 customer records with 20 features and a binary `Churn` target.

### Model Architecture / Tech Stack

```
Customer Account & Usage Data (20 features)
→ Encoding + Preprocessing
→ PyCaret AutoML (model comparison + selection)
→ Churn Prediction: Yes / No
```

**Tech Stack:** Python · PyCaret · scikit-learn · pandas · NumPy · joblib · Streamlit

### How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

Enter customer account details in the Streamlit app to predict whether the customer is at risk of churning.

### Requirements

```
pycaret
pandas
numpy
scikit-learn
streamlit
joblib
```

---

## Türkçe

### Hakkında

Bu proje, müşteri kaybını tahmin etmek için en iyi sınıflandırıcıyı otomatik olarak seçmek ve eğitmek amacıyla IBM Telco Müşteri Kaybı veri setine PyCaret AutoML uygular. Özellikler arasında sözleşme türü, aylık ücretler, müşteri süresi, internet hizmeti türü ve destek abonelikleri yer alır.

### Özellikler

- İkili sınıflandırma: Churn = Evet / Hayır
- Giriş özellikleri: müşteri süresi, sözleşme türü, aylık ücretler, toplam ücretler, internet hizmeti, ödeme yöntemi, destek eklentileri, telefon/çoklu hatlar
- PyCaret AutoML model seçimi ve eğitimi
- Kaydedilen en iyi model: `best_automl_model.pkl`
- Müşteri kaybı riski değerlendirmesi için Streamlit web uygulaması

### Veri Seti

**Kaynak:** [Kaggle — Telco Müşteri Kaybı](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

| Dosya | Boyut | Durum |
|---|---|---|
| `WA_Fn-UseC_-Telco-Customer-Churn.csv` | 0,93 MB | ✅ Dahil |
| `train.csv` | 0,68 MB | ✅ Dahil |
| `test.csv` | 0,17 MB | ✅ Dahil |

20 özellik ve ikili `Churn` hedefiyle 7.043 müşteri kaydı.

### Model Mimarisi / Teknoloji Yığını

```
Müşteri Hesap & Kullanım Verisi (20 özellik)
→ Kodlama + Ön İşleme
→ PyCaret AutoML (model karşılaştırma + seçim)
→ Churn Tahmini: Evet / Hayır
```

**Teknoloji Yığını:** Python · PyCaret · scikit-learn · pandas · NumPy · joblib · Streamlit

### Nasıl Çalıştırılır

```bash
pip install -r requirements.txt
streamlit run app.py
```

Streamlit uygulamasına müşteri hesap bilgilerini girerek müşterinin ayrılma riskini tahmin edin.

### Gereksinimler

```
pycaret
pandas
numpy
scikit-learn
streamlit
joblib
```
