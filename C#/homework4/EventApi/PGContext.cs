﻿using Microsoft.EntityFrameworkCore;
using Npgsql;
using System;


namespace EventApi
{
    public class PGContext : DbContext
    {
        public PGContext() { }
        public PGContext(DbContextOptions<PGContext> options) : base(options) { }
        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            optionsBuilder.UseNpgsql(Environment.GetEnvironmentVariable("ConString"));
            NpgsqlConnection.GlobalTypeMapper.MapEnum<RestaurantNames>("RestaurantNames");
            NpgsqlConnection.GlobalTypeMapper.MapComposite<Event>("Events");
        }

        public DbSet<Event> Events { get; set; }
    }
}
