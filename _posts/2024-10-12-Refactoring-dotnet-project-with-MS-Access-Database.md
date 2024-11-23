---
layout: post
title: Refactoring a .NET Project with MS Access Database
subtitle: Refactoring
tags: [technology]
comments: false
---

# Refactoring a .NET Project with MS Access Database

## Overview

### **Current Situation**
- Relies on MS Access as the database.
- Heavy use of raw SQL strings in the code.
- Limited flexibility for switching databases.
- Potential performance and security issues.

### **Goals of Refactoring**
1. Use an ORM framework to abstract database operations.
2. Enable seamless switching to SQLite or SQL Server.
3. Identify and fix vulnerabilities in the old system.
4. Improve program execution efficiency and maintainability.

---

## Benefits of Using an ORM Framework

1. **Database Independence**:
   - Easily switch between databases (e.g., SQLite, SQL Server).
2. **Code Simplification**:
   - Replace raw SQL with higher-level abstractions.
3. **Security Enhancements**:
   - Prevent SQL injection and manage sensitive data securely.
4. **Performance Optimization**:
   - Support batch operations, caching, and optimized queries.
5. **Maintainability**:
   - Easier to debug, test, and extend.

---

## Step 1: Analyze the Existing Project

1. **Codebase Analysis**:
   - Identify all occurrences of hardcoded SQL strings.
   - List functions relying on MS Access-specific features.

2. **Database Structure**:
   - Review table schemas, relationships, and data types.
   - Analyze dependencies like stored procedures or triggers.

3. **Pain Points**:
   - Performance bottlenecks.
   - Risks of SQL injection or unencrypted sensitive data.

---

## Step 2: Introducing an ORM Framework

### **Entity Framework Core**
- **Features**:
  - Supports multiple databases (SQLite, SQL Server, etc.).
  - Provides migration tools for schema evolution.
  - Simplifies data access with LINQ.

#### Configuring Multi-Database Support
In `appsettings.json`:
```json
{
  "ConnectionStrings": {
    "SQLite": "Data Source=app.db",
    "SqlServer": "Server=myServerAddress;Database=myDataBase;User Id=myUsername;Password=myPassword;"
  }
}
```

Select the database based on configuration:
```csharp
var builder = new DbContextOptionsBuilder<MyDbContext>();
var databaseType = Configuration["DatabaseType"];

if (databaseType == "SQLite")
    builder.UseSqlite(Configuration.GetConnectionString("SQLite"));
else if (databaseType == "SqlServer")
    builder.UseSqlServer(Configuration.GetConnectionString("SqlServer"));
```

---

## Step 3: Refactor Data Access Layer

### **Replace Raw SQL with ORM Queries**
#### Before (Raw SQL):
```csharp
string query = "SELECT * FROM Users WHERE Name = '" + userName + "'";
var command = new OleDbCommand(query, connection);
```

#### After (Using EF Core):
```csharp
var user = dbContext.Users.Where(u => u.Name == userName).FirstOrDefault();
```

### **Implement Repository and Unit of Work Patterns**
Example Repository:
```csharp
public interface IUserRepository
{
    Task<User> GetUserByNameAsync(string name);
}

public class UserRepository : IUserRepository
{
    private readonly MyDbContext _context;
    public UserRepository(MyDbContext context) => _context = context;

    public async Task<User> GetUserByNameAsync(string name)
    {
        return await _context.Users.FirstOrDefaultAsync(u => u.Name == name);
    }
}
```

---

## Step 4: Data Migration

1. **Export Existing Data**:
   - Use tools like **Access to SQL Server Migration Tool**.
   - Alternatively, export data as CSV and import into the new database.

2. **Set Up Database with EF Core**:
   - Use migrations to create the database schema:
     ```bash
     dotnet ef migrations add InitialCreate
     dotnet ef database update
     ```

3. **Test Migration Results**:
   - Verify data accuracy in SQLite or SQL Server.

---

## Step 5: Fix Vulnerabilities

### **1. Eliminate SQL Injection**
- Replace concatenated SQL with parameterized queries or ORM methods.

### **2. Secure Sensitive Data**
- Hash passwords (e.g., use BCrypt).
- Avoid storing sensitive information in plaintext.

### **3. Validate User Input**
- Sanitize and validate inputs to prevent malicious entries.

### **4. Manage Resources Properly**
- Use `using` statements to handle database connections.

---

## Step 6: Performance Optimization

1. **Batch Operations**:
   - Replace iterative insert/update logic with batch processing.

2. **Lazy vs. Eager Loading**:
   - Use `Include` for eager loading when necessary.
   - Enable lazy loading for large datasets to reduce memory usage.

3. **Caching**:
   - Cache frequently accessed but rarely updated data using `IMemoryCache`.

4. **Index Optimization**:
   - Analyze query patterns and create appropriate indexes.

---

## Step 7: Enable Database Switching

1. **Dynamic Database Selection**:
   - Use environment variables or configuration files to select the database at runtime.

2. **Testing Across Databases**:
   - Test all functionality with both SQLite and SQL Server to ensure compatibility.

---

## Step 8: Enhance Maintainability

1. **Modularize Code**:
   - Separate data access, business logic, and presentation layers.
   - Use dependency injection for better control over service lifetimes.

2. **Unit Testing**:
   - Use in-memory databases for testing (e.g., EF Core InMemory).

3. **CI/CD Integration**:
   - Automate database migrations and regression tests in CI/CD pipelines.

---

## Comparison Before and After Refactoring

| **Aspect**           | **Before**                 | **After**                            |
|-----------------------|---------------------------|---------------------------------------|
| **Database**          | MS Access                | SQLite / SQL Server                  |
| **SQL Usage**         | Raw SQL strings          | ORM-based queries                    |
| **Security**          | High risk of SQL injection | Secure parameterized queries         |
| **Flexibility**       | Tied to Access           | Supports multiple databases          |
| **Performance**       | Inefficient, repetitive queries | Optimized with caching and indexing |
| **Maintainability**   | Hard to debug            | Modular and testable code            |

---

## Summary

1. **ORM Benefits**: Simplifies database operations, enhances security, and improves maintainability.
2. **Flexibility**: Supports both SQLite (lightweight) and SQL Server (enterprise-grade).
3. **Optimizations**: Introduced caching, indexing, and efficient queries.
4. **Next Steps**: Continuously test and refine the system for performance and reliability.

--- 