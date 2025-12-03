// Generate random name
const names = ['john', 'jane', 'mike', 'sarah', 'david', 'emma', 'chris', 'lisa', 'tom', 'anna', 'alex', 'sam', 'jordan', 'taylor', 'morgan'];
const randomName = names[Math.floor(Math.random() * names.length)];

// Generate random email (same as name)
const randomEmail = randomName + '@yopmail.com';

// Generate random phone
const randomPhone = '+1 ' + Math.floor(Math.random() * 900 + 100) + ' ' + Math.floor(Math.random() * 900 + 100) + ' ' + Math.floor(Math.random() * 9000 + 1000);

// Generate random address
const streets = ['Main St', 'Oak Ave', 'Pine Rd', 'Maple Dr', 'Cedar Ln', 'Elm St', 'Park Ave', 'Lake Rd'];
const randomAddress = Math.floor(Math.random() * 9999 + 1) + ' ' + streets[Math.floor(Math.random() * streets.length)];

// Set environment variables
pm.environment.set('name', randomName);
pm.environment.set('email', randomEmail);
pm.environment.set('phone', randomPhone);
pm.environment.set('address', randomAddress);

/* body json

{
    "name": "{{name}}",
    "email": "{{email}}",
    "phone": "{{phone}}",
    "address": "{{address}}",
    "tagIds": [
        "42777115-6f69-4f52-b22f-9473ea2c0af9"
    ]
} */