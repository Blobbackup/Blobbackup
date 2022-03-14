<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class Add2FacColumnsToUsersTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::table('users', function (Blueprint $table) {
            $table->boolean('twofac')->default(false);
            $table->string('backup_code')->nullable();
            $table->string('phone')->nullable();
            $table->string('totp_secret')->nullable();
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::table('users', function (Blueprint $table) {
            $table->dropColumn('twofac');
            $table->dropColumn('backup_code');
            $table->dropColumn('phone');
            $table->dropColumn('totp_secret');
        });
    }
}
