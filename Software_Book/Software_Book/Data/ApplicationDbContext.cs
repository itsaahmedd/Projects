using Microsoft.AspNetCore.Identity.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore;
using Software_Book.Models;


namespace Software_Book.Data;

public class ApplicationDbContext : IdentityDbContext
{
    public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options)
        : base(options)
    {

    }


    public DbSet<Appointment_1> Appointments_1 { get; set; }

    public DbSet<Appointment_2> Appointments_2 { get; set; }

    public DbSet<Appointment_3> Appointments_3 { get; set; }



}

