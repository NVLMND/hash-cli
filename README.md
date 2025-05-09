# Password Hasher CLI

A lightweight Python CLI tool to hash passwords using **MD5**, **SHA-256**, or **SHA-512**, with optional salting.

## Features

- Supports **MD5**, **SHA-256**, and **SHA-512**
- Optional salt integration
- Minimal dependencies (only uses Python standard libraries)
- Secure and straightforward command-line usage

## Usage

```bash
python hash.py -p YOUR_PASSWORD -a [md5|sha256|sha512] [-s OPTIONAL_SALT]
```

### Example : Hash with salt
```bash
python hash.py -p 696969 -a sha512 -s abc
```

## Output

```bash
Hashed password: 1018ce1bbb7dca3b3f68af95b9ba9cc83e306d6a982f0593d1db2137c63b16c330a16afad52ca0874eb14fb001827c59fb003c422ffe3269949960db484ac4ff

it's MASSIVE!!!
```
