using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Software_Book.Data;
using Software_Book.Models;

// For more information on enabling MVC for empty projects, visit https://go.microsoft.com/fwlink/?LinkID=397860

namespace Software_Book.Controllers
{

    public class AppointmentController : Controller
    {
        private readonly ApplicationDbContext _dbContext;

        public AppointmentController(ApplicationDbContext dbContext)
        {
            _dbContext = dbContext;
        }

        // GET: /<controller>/


        public IActionResult Calander()
        {

            return View();
        }


        public IActionResult Appointments()
        {
            var appointments_1 = _dbContext.Appointments_1.ToList();


            return Json(appointments_1);
        }


        public IActionResult Appointments_2()
        {


            var appointments_2 = _dbContext.Appointments_2.ToList();


            return Json(appointments_2);
        }


        public IActionResult Appointments_3()
        {


            var appointments_3 = _dbContext.Appointments_3.ToList();


            return Json(appointments_3);
        }






        [HttpPost]
        public IActionResult create_Calander_1(Appointment_1 appointment_1)
        {

            _dbContext.Appointments_1.Add(appointment_1);
            _dbContext.SaveChanges();
            return View();
        }



        [HttpPost]
        public IActionResult create_Calander_2(Appointment_2 appointment_2)
        {

            _dbContext.Appointments_2.Add(appointment_2);
            _dbContext.SaveChanges();
            return View();
        }




        [HttpPost]
        public IActionResult create_Calander_3(Appointment_3 appointment_3)
        {

            _dbContext.Appointments_3.Add(appointment_3);
            _dbContext.SaveChanges();
            return View();
        }


        [HttpPost]
        public IActionResult cancelAppointment_1(string username)
        {
            var appointment = _dbContext.Appointments_1.FirstOrDefault(a => a.customer == username);

            if (appointment != null)
            {
                _dbContext.Appointments_1.Remove(appointment);
                _dbContext.SaveChanges();
                return Json(new { success = true, message = "Appointment canceled successfully." });
            }

            return Json(new { success = false, message = "Appointment not found." });
        }



        [HttpPost]
        public IActionResult cancelAppointment_2(string username)
        {
            var appointment = _dbContext.Appointments_2.FirstOrDefault(a => a.customer == username);

            if (appointment != null)
            {
                _dbContext.Appointments_2.Remove(appointment);
                _dbContext.SaveChanges();
                return Json(new { success = true, message = "Appointment canceled successfully." });
            }

            return Json(new { success = false, message = "Appointment not found." });
        }



        [HttpPost]
        public IActionResult cancelAppointment_3(string username)
        {
            var appointment = _dbContext.Appointments_3.FirstOrDefault(a => a.customer == username);

            if (appointment != null)
            {
                _dbContext.Appointments_3.Remove(appointment);
                _dbContext.SaveChanges();
                return Json(new { success = true, message = "Appointment canceled successfully." });
            }

            return Json(new { success = false, message = "Appointment not found." });
        }


    }
}