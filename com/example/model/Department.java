package com.example.model;

public class Department {
    private String deptName;

    public Department(String deptName) {
        this.deptName = deptName;
    }

    public void showDept() {
        System.out.println("Department: " + deptName);
    }
}

