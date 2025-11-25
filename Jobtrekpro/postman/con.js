// Utility helpers
function pick(arr) { return arr[Math.floor(Math.random() * arr.length)]; }

function randomDOB() {
    const today = new Date();
    const years = Math.floor(Math.random() * 45) + 21;
    today.setFullYear(today.getFullYear() - years);
    today.setDate(today.getDate() - Math.floor(Math.random() * 365));
    return today.toISOString().split("T")[0];
}

// Data pools
const FIRST = [
    'John', 'Michael', 'David', 'James', 'Robert', 'William',
    'Sarah', 'Jennifer', 'Lisa', 'Mary', 'Patricia', 'Linda',
    'Ahmed', 'Ali', 'Hassan', 'Fatima', 'Aisha', 'Zainab',
    'Chris', 'Daniel', 'Matthew', 'Emma', 'Olivia', 'Sophia',
    'Illana', 'Carlos', 'Marcus', 'Elena', 'Diego', 'Isabella'
];

const LAST = [
    'Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia',
    'Miller', 'Davis', 'Rodriguez', 'Martinez', 'Hernandez',
    'Khan', 'Ahmed', 'Ali', 'Hassan', 'Malik', 'Shah',
    'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson',
    'Dickson', 'Cooper', 'Bennett', 'Foster', 'Coleman'
];

const ADDRESSES = [
    "123 Main Street", "456 Oak Avenue", "789 Elm Boulevard",
    "321 Pine Road", "654 Maple Drive", "987 Cedar Lane",
    "147 Birch Street", "258 Willow Way", "369 Aspen Court",
    "741 Spruce Avenue"
];

const TAG_NAMES = [
    "urgent", "vip", "priority", "certified", "active",
    "verified", "expert", "reliable", "preferred", "new-hire"
];

const TAG_COLORS = [
    '#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8',
    '#F7DC6F', '#BB8FCE', '#85C1E2', '#F8B195', '#C06C84',
    '#6C5B7B', '#355C7D', '#F67280', '#C8E6C9', '#FFCCBC',
    '#0055ff', '#ff5500', '#00ff55', '#5500ff', '#ff0055'
];

const SPECIALIZATIONS = [
    "electrical", "plumbing", "hvac", "carpentry",
    "painting", "roofing", "cleaning", "landscaping"
];

const SKILLS = ["beginner", "intermediate", "advanced", "expert"];
const VEHICLES = ["car", "truck", "van", "suv"];

// Generate random fields
let first = pick(FIRST);
let last = pick(LAST);

let index = Math.floor(Math.random() * 100);
let email = `t+${index}@yopmail.com`;

let hasVehicle = Math.random() < 0.3;

// Set Postman variables
pm.variables.set("first", first);
pm.variables.set("last", last);
pm.variables.set("email", email);

pm.variables.set("phone", `+1 (${Math.floor(100 + Math.random() * 899)}) ${Math.floor(1000000 + Math.random() * 8999999)}`);
pm.variables.set("dateOfBirth", randomDOB());
pm.variables.set("address", pick(ADDRESSES));

pm.variables.set("serviceRadius", pick([10, 15, 25, 30, 50]));
pm.variables.set("hourlyRate", Math.floor(Math.random() * 80) + 20);
pm.variables.set("yearsExperience", Math.floor(Math.random() * 40) + 1);

pm.variables.set("skillLevel", pick(SKILLS));
pm.variables.set("specialization", pick(SPECIALIZATIONS));

pm.variables.set("hasVehicle", hasVehicle);
pm.variables.set("vehicleType", hasVehicle ? pick(VEHICLES) : "");

pm.variables.set("ownsTools", Math.random() < 0.5);

pm.variables.set("tagName", pick(TAG_NAMES));
pm.variables.set("tagColor", pick(TAG_COLORS));
